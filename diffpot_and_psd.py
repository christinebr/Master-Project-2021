import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from diffusionpotential import DiffusionPotential

# This file uses scenario 1 (delta_K + delta_Na = delta_Cl) to find the
# initial concentrations. For each concentration data I initialize an instance
# of the # DiffusionPotential class. Each class instance gets their initial
# diffusion potential and their exponential decay calculated. At last the
# PSD of the exponential decaying potential is calculated.
# This file generates two plot: one for the exponentially decaying potential
# and one for the PSDs of that potential.
# At last the exponentially decaying diffusion potential, the calculated PSD
# and corresponding frequency array is saved to a .csv file for later use.


def scenario1(k=None, na=None, kbase=3.0, nabase=146.0):
    """
    Using scenario 1 to calculate initial concentration difference for K, Na
    and Cl.

    :param k: [int or float] concentration change in K
    :param na: [int or float] concentration change in Na
    :param kbase: [int or float] baseline concentration for K
    :param nabase: [int or float] baseline concentration for Na

    :return: init_c: [dict] dictionary with K, Na and Cl as keys and
                            structured as: {'ion': [base, base+/-change]}
    """
    clbase = kbase + nabase
    init_c = None
    if k:
        init_c = {'K': [kbase, kbase+k],
                  'Na': [nabase, nabase-k],
                  'Cl': [clbase, clbase]}
    elif na:
        init_c = {'K': [kbase, kbase+na],
                  'Na': [nabase, nabase-na],
                  'Cl': [clbase, clbase]}
    if k and na:
        init_c = {'K': [kbase, kbase+k],
                  'Na': [nabase, nabase-na],
                  'Cl': [clbase, clbase+k-na]}
    return init_c


dt = 0.01
t_end = 100

# ========================= Dietzel 1982 ======================================
# recording in the sensorimotor cortex of cats, simulation on cortical surface
TAU = 10
t = f", \u03C4={TAU}"
# Dietzel 1982 Figure 3 - depth profile of Na
c1 = scenario1(na=5.9, nabase=146)
Dietzel1 = DiffusionPotential(conc=c1, tau=TAU, delta_t=dt, t_end=t_end,
                              name='DietzelFig3'+t)
# Dietzel 1982 Figure 4A - recorded Na and K in 100 micro meters depth
c2 = scenario1(k=6, na=15, kbase=3, nabase=149)
Dietzel2 = DiffusionPotential(conc=c2, tau=TAU, delta_t=dt, t_end=t_end,
                              name='DietzelFig4A100'+t)
# Dietzel 1982 Figure 4A - recorded Na and K in 1000 micro meters depth
c3 = scenario1(k=6, na=7, kbase=3, nabase=149)
Dietzel3 = DiffusionPotential(conc=c3, tau=TAU, delta_t=dt, t_end=t_end,
                              name='DietzelFig4A1000'+t)

data = [Dietzel1, Dietzel2, Dietzel3]


# ========================= Haj-Yasein 2015 ===================================
# 10s simulation at 20 Hz
TAU = 5
t = f", $\u03C4$={TAU}"
# Figure 2a - recordings in hippocampal synaptic stratum radiatum layer CA1
c1 = scenario1(k=4.75, kbase=3.25, nabase=149)
HajYasein1 = DiffusionPotential(conc=c1, tau=TAU, delta_t=dt, t_end=t_end,
                                name='Haj-YaseinFig2a'+t)
# Figure 2b - recodings from the stratum pyramidale
c2 = scenario1(k=9.25, kbase=3.25, nabase=149)
HajYasein2 = DiffusionPotential(conc=c2, tau=TAU, delta_t=dt, t_end=t_end,
                                name='Haj-YaseinFig2b' + t)

data.extend([HajYasein1, HajYasein2])


# ================== Cordingley 1978 (Graity2017) =============================
# Cordingley Figure 5 (Graity Figure 2B) - depth profile, recorded in cat
# visual cortex, electrical stimulation of the thalamus
TAU = 5
t = f", $\u03C4$={TAU}"
c1 = scenario1(k=1.891, kbase=2.735, nabase=149)
Cordingley = DiffusionPotential(conc=c1, tau=TAU, delta_t=dt, t_end=t_end,
                                name='CordingleyFig2B'+t)
data.append(Cordingley)


# ========================= Sykova 1983 =======================================
# Figure 3A - recorded in L7 spinal cord of cat, tetanic simulation of
# posterier tibial nerve
TAU = 11.8
t = f", $\u03C4$={TAU}"
c1 = scenario1(k=6, kbase=3, nabase=149)
SykovaFig3A = DiffusionPotential(conc=c1, tau=TAU, delta_t=dt, t_end=t_end,
                                 name='SykovaFig3A'+t)
# Figure 14A - recorded in rat cerebellum, simulation at 20 Hz
TAU = 10
t = f", $\u03C4$={TAU}"
c2 = scenario1(k=5, kbase=3, nabase=149)
SykovaFig14A = DiffusionPotential(conc=c2, tau=TAU, delta_t=dt, t_end=t_end,
                                  name='SykovaFig14A'+t)

data.extend([SykovaFig3A, SykovaFig14A])


# ========================= Mccreery 1983 =====================================
# Figure 2B - recorded 750 micro meter beneath an electrode injection
TAU = 30
t = f", $\u03C4$={TAU}"
c1 = scenario1(k=4, kbase=3, nabase=149)
MccreeryFig2B = DiffusionPotential(conc=c1, tau=TAU, delta_t=dt, t_end=t_end,
                                   name='MccreeryFig2B'+t)
data.append(MccreeryFig2B)


# ========================= Halnes 2016 =======================================
# simulation, depth profile (Videm 2018, Figure 2.4)
TAU = 30
t = f", $\u03C4$={TAU}"
c1 = scenario1(k=5.999, kbase=3, nabase=149)
Halnes2016 = DiffusionPotential(conc=c1, tau=TAU, delta_t=dt, t_end=t_end,
                                name='Halnes2016'+t)
data.append(Halnes2016)


# ========================= Nicholson1987  ====================================
# Figure 4, depth profile
TAU = 30
t = f", $\u03C4$={TAU}"
c1 = scenario1(k=4.4, kbase=3, nabase=149)
Nicholson1987 = DiffusionPotential(conc=c1, tau=TAU, delta_t=dt, t_end=t_end,
                                   name='NicholsonFig4'+t)
data.append(Nicholson1987)


# ========================= Octeau 2019 =======================================
# Figure 1G
TAU = 6.1
t = f", $\u03C4$={TAU}"
c1 = scenario1(k=0.9, kbase=4.5, nabase=149)
Octeau2019 = DiffusionPotential(conc=c1, tau=TAU, delta_t=dt, t_end=t_end,
                                name='OcteauFig1G'+t)
data.append(Octeau2019)

# ========================= Amzica 2002 =======================================
# Figure 3A, oscillation
TAU = 20
t = f", $\u03C4$={TAU}"
c1 = scenario1(k=0.6, kbase=3.4, nabase=149)
Amzica2002 = DiffusionPotential(conc=c1, tau=TAU, delta_t=dt, t_end=t_end,
                                name='AmzicaFig3A'+t)
data.append(Amzica2002)

# ========================= Frölich 2008 ======================================
# Figure 1B, oscillation
TAU = 20
t = f", $\u03C4$={TAU}"
c1 = scenario1(k=1.6, kbase=3, nabase=149)
Frolich2008 = DiffusionPotential(conc=c1, tau=TAU, delta_t=dt, t_end=t_end,
                                 name='FrolichFig1B'+t)
data.append(Frolich2008)

# =============================================================================
#                             PLOTTING
# =============================================================================
# Plot diffusion potential
plt.figure()
for model in data:
    model.calculate_everything()
    plt.plot(model.t, model.exp_decay, '--', label=model.name)
plt.xlabel('time [s]')
plt.ylabel('potential [mV]')
plt.title('Diffusion potential')
plt.legend(loc='upper right', ncol=2)
plt.savefig('Figures/diff_pot', dpi=500)
plt.show()

# Plot PSD of diffusion potential
plt.figure(figsize=(9.6, 4.8))
for model in data:
    plt.plot(np.log10(model.f), np.log10(model.psd), '--',
             linewidth=1, label=model.name)
plt.xlabel('log$_{10}$(frequency) [Hz]')
plt.ylabel('log$_{10}$(PSD) [mV$^{2}$/Hz]')
plt.title('PSDs of diffusion potential')
plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")  # outside right
plt.savefig('Figures/psd_of_diff_pot', dpi=500)
plt.show()

# =============================================================================
#             Saving potential data and psd data for later use
# =============================================================================
pot_data = {}  # dictionary for potential data
psd_data = {}  # dictionary for psd data
for model in data:
    pot_data[str(model.name)] = {'t': model.t,
                                 'exp_pot': model.exp_decay}
    psd_data[str(model.name)] = {'f': model.f,
                                 'psd': model.psd}
df_pot_data = pd.DataFrame(data=pot_data)  # making DataFrame
df_pot_data.to_csv("Data_PSD_other/potential_data_normal.csv")  # save to file

df_psd_data = pd.DataFrame(data=psd_data)  # making DataFrame
df_psd_data.to_csv("Data_PSD_other/psd_data_normal.csv")  # save to file
