import numpy as np
from scipy.signal import periodogram

# This file contains two classes: Ion and DiffusionPotential.
# Ion stores variables associated to a specified ion species.
# DiffusionPotential calculates and stores everything needed to calculate the
# power spectrum density of a diffusion potential

# Constants
R = 8.3144598  # gas constant, J / mol K
F = 96485.333  # Faraday's constant, s A / mol
lambda_n = 1.6  # tortuosity


class Ion:
    def __init__(self, c, d, z, name):
        """
        The class stores variables for one ion species.
        :param c: initial concentration of ion
        :param d: diffusion coefficient
        :param z: valence of ion
        :param name: name of ion
        """
        self.c = np.asarray(c, dtype=np.float)  # concentration
        self.D = d / (lambda_n ** 2)  # diffusion constant in ECS
        self.z = z  # valence
        self.name = name  # name of the ion


# valence for each ion
valence = {'K': +1, 'Na': +1, 'Cl': -1,
           'Ca': +2, 'Mg': +2, 'HCO3': -1}

# diffusion coefficients, m^2 / s
diffcoeff = {'K': 1.96e-9, 'Na': 1.33e-9, 'Cl': 2.03e-9,
             'Ca': 0.71e-9, 'Mg': 0.72e-9, 'HCO3': 1.18e-9}


class DiffusionPotential:
    def __init__(self, conc, tau, delta_t, t_end, name, temp=310):
        """
        :param conc: dict with K, Na and Cl as keys
        """
        self.T = temp  # temperature, K
        self.name = name
        self.ion_list = [Ion(c=conc[ion], d=diffcoeff[ion],
                             z=valence[ion], name=ion)
                         for ion in conc.keys()]
        self.tau = tau
        self.delta_t = delta_t
        self.t_end = t_end
        self.goldman = None
        self.henderson = None
        self.delta_phi = None
        self.potential = np.array([self.goldman, self.henderson,
                                   self.delta_phi])
        self.exp_decay, self.t = None, None
        self.psd, self.f = None, None

    def goldman_eq(self):
        """potential in milli-volt [mV]"""
        numerator_sum = 0
        denominator_sum = 0
        for ion in self.ion_list:  # loop through each ion
            if ion.z > 0:  # a positive ion c = [min, max]
                numerator_sum += ion.D * ion.c[0]  # "outside" = box 1
                denominator_sum += ion.D * ion.c[1]  # "inside" = box 0
            else:  # negative ion
                numerator_sum += ion.D * ion.c[1]  # "inside" = box 0
                denominator_sum += ion.D * ion.c[0]  # "outside" = box 1
        self.goldman = (R * self.T / F) * \
                       (np.log(numerator_sum / denominator_sum)) * 1000

    def henderson_eq(self):
        """potential in milli-volt [mV]"""
        num_sum = 0
        denom_sum = 0
        num_ln = 0
        denom_ln = 0
        for ion in self.ion_list:  # loop through each ion
            num_sum += ion.D * abs(ion.z) / ion.z * (ion.c[1] - ion.c[0])
            denom_sum += ion.D * abs(ion.z) * (ion.c[1] - ion.c[0])
            num_ln += ion.D * abs(ion.z) * ion.c[0]
            denom_ln += ion.D * abs(ion.z) * ion.c[1]
        self.henderson = (R * self.T / F) * (num_sum / denom_sum) * \
                         (np.log(num_ln / denom_ln)) * 1000

    def average_sigma(self):
        psi = (R * self.T) / F
        summation = 0
        for ion in self.ion_list:
            # ion c = [min, max]
            summation += ion.D * (ion.z ** 2) * (ion.c[0] + ion.c[1]) / 2
        return (F / psi) * summation

    def delta_phi_eq(self):
        """potential in milli-volt [mV]"""
        summation = 0
        for ion in self.ion_list:
            summation += ion.D * (ion.z ** 2) * (ion.c[1] - ion.c[0])
        self.delta_phi = (F / self.average_sigma()) * summation * 1000

    def exponential_decay(self, g=False, h=False):
        self.t = np.linspace(0, self.t_end, num=int(self.t_end / self.delta_t))
        if g:
            init_potential = self.goldman
        elif h:
            init_potential = self.henderson
        else:
            init_potential = self.delta_phi
        self.exp_decay = abs(init_potential) * np.exp(-self.t / self.tau)

    def power_spectrum_density(self):
        fs = 1 / self.delta_t
        self.f, self.psd = periodogram(self.exp_decay, fs)

    def calculate_everything(self, goldman=False, henderson=False):
        # Calculate initial potential
        self.goldman_eq()
        self.henderson_eq()
        self.delta_phi_eq()

        # Letting the potential decay exponentially
        if goldman:
            self.exponential_decay(g=goldman)
        elif henderson:
            self.exponential_decay(h=henderson)
        else:
            self.exponential_decay()

        # Calculating the power spectrum density
        self.power_spectrum_density()
