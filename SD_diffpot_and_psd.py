import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from diffusionpotential import DiffusionPotential

DELTA_T = 0.01
T_END = 100


def scenario4(k=None, na=None, kbase=3.0, nabase=146.0):
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
                  'Na': [nabase, nabase-2*k],
                  'Cl': [clbase, clbase-k]}
    elif na:
        init_c = {'K': [kbase, kbase+0.5*na],
                  'Na': [nabase, nabase-na],
                  'Cl': [clbase, clbase-0.5*na]}
    return init_c


# =============================================================================
#                          SPREADING DEPRESSION
# =============================================================================
data_SD = []
# =========== Enger2015 ===================================================
# cortical spreading depression in the visual cortex of adult living mice
TAU = 50
t = f", $\u03C4$={TAU}"
delta_k = 19
c1 = scenario4(k=delta_k, kbase=3, nabase=149)
EngerFig4F = DiffusionPotential(conc=c1, tau=TAU, delta_t=DELTA_T, t_end=T_END,
                                name='EngerFig4F'+t)

delta_k = 23
c1 = scenario4(k=delta_k, kbase=3, nabase=149)
EngerFig4G = DiffusionPotential(conc=c1, tau=TAU, delta_t=DELTA_T, t_end=T_END,
                                name='EngerFig4G'+t)

delta_k = 28
c1 = scenario4(k=delta_k, kbase=3, nabase=149)
EngerFig4H = DiffusionPotential(conc=c1, tau=TAU, delta_t=DELTA_T, t_end=T_END,
                                name='EngerFig4H'+t)
data_SD.extend([EngerFig4F, EngerFig4G, EngerFig4H])

# =========== Herreras2020 ===================================================
# spreading depression in CA1 strata (hippocampus)
TAU = 30
t = f", $\u03C4$={TAU}"
delta_k = 51
c1 = scenario4(k=delta_k, kbase=3, nabase=149)
HerrerasFig1 = DiffusionPotential(conc=c1, tau=TAU, delta_t=DELTA_T, t_end=T_END,
                                  name='HerrerasFig1'+t)
data_SD.append(HerrerasFig1)

# =========== Sykova1983 ===================================================
# Figure 14 B - spreading depression in rat cerebellum
TAU = 10.2
t = f", $\u03C4$={TAU}"
delta_k = 32
c1 = scenario4(k=delta_k, kbase=3, nabase=149)
SykovaFig14B = DiffusionPotential(conc=c1, tau=TAU, delta_t=DELTA_T, t_end=T_END,
                                  name='SykovaFig14B'+t)

# Figure 24 - spreading depression in rat cerebellum
TAU = 5*60
t = f", $\u03C4$={TAU}"
delta_k = 40
c1 = scenario4(k=delta_k, kbase=3, nabase=149)
SykovaFig24 = DiffusionPotential(conc=c1, tau=TAU, delta_t=DELTA_T, t_end=T_END,
                                 name='SykovaFig24'+t)
data_SD.extend([SykovaFig14B, SykovaFig24])

# =========== Hansen1981 ===================================================
# Figure 1 - spreading depression elicted by a brief needle stab in the frontal
# cortex
TAU = 12
t = f", $\u03C4$={TAU}"
delta_k = 53
c1 = scenario4(k=delta_k, kbase=3, nabase=149)
HansenFig1 = DiffusionPotential(conc=c1, tau=TAU, delta_t=DELTA_T, t_end=T_END,
                                name='HansenFig1'+t)
data_SD.append(HansenFig1)

# Figure 2 - spreading depression
TAU = 12
t = f", $\u03C4$={TAU}"
delta_k = 50
c1 = scenario4(k=delta_k, kbase=3, nabase=149)
HansenFig2 = DiffusionPotential(conc=c1, tau=TAU, delta_t=DELTA_T, t_end=T_END,
                                name='HansenFig2'+t)
data_SD.append(HansenFig2)

# =========== Kraig1983 ===================================================
# Figure 4 - spreading depression, cerebellar molecular layer of the catfish
TAU = 4*60
t = f", $\u03C4$={TAU}"
delta_k = 38
c1 = scenario4(k=delta_k, kbase=3, nabase=149)
KraigFig4 = DiffusionPotential(conc=c1, tau=TAU, delta_t=DELTA_T, t_end=T_END,
                               name='KraigFig4'+t)
data_SD.append(KraigFig4)

# ========================= Amzica 2002 =======================================
# Figure 6B, spike-wave seizures
TAU = 20
t = f", $\u03C4$={TAU}"
delta_k = 8.25
c1 = scenario4(k=delta_k, kbase=3, nabase=149)
AmzicaFig6B = DiffusionPotential(conc=c1, tau=TAU, delta_t=DELTA_T, t_end=T_END,
                                 name='AmzicaFig6B'+t)
# Figure 7, spike-wave seizures
TAU = 20
t = f", $\u03C4$={TAU}"
delta_k = 6.5
c1 = scenario4(k=delta_k, kbase=3, nabase=149)
AmzicaFig7 = DiffusionPotential(conc=c1, tau=TAU, delta_t=DELTA_T, t_end=T_END,
                                name='AmzicaFig7'+t)
data_SD.extend([AmzicaFig6B, AmzicaFig7])


# ========================= Frölich 2008 ======================================
# Figure 7, spike-wave seizures
TAU = 20
t = f", $\u03C4$={TAU}"
delta_k = 7
c1 = scenario4(k=delta_k, kbase=3, nabase=149)
FrolichFig1C = DiffusionPotential(conc=c1, tau=TAU, delta_t=DELTA_T, t_end=T_END,
                                  name='FrolichFig1C'+t)
data_SD.append(FrolichFig1C)

# ========================= Raimondo ======================================
# Figure 1, during seizure
TAU = 20
t = f", $\u03C4$={TAU}"
delta_k = 11
c1 = scenario4(k=delta_k, kbase=4, nabase=149)
RaimondoFig1 = DiffusionPotential(conc=c1, tau=TAU, delta_t=DELTA_T, t_end=T_END,
                                  name='RaimondoFig1'+t)
data_SD.append(RaimondoFig1)

# ========================= Nicholson 1980 ====================================


# ========================= Hertz 2013 ======================================
# Figure 6, epileptic

# =============================================================================
#                       PLOTTING - Spreading Depression
# =============================================================================
# Plot diffusion potential
plt.figure()
for model in data_SD:
    model.calculate_everything()
    plt.plot(model.t, model.exp_decay, '-.', label=model.name)
plt.xlabel('time [s]')
plt.ylabel('potential [mV]')
plt.title('SD (Spreading Depression) diffusion potential')
plt.legend(loc='upper right', ncol=2)
plt.savefig('Figures/SD_diff_pot', dpi=500)
plt.show()

# Plot PSD of diffusion potential
plt.figure(figsize=(9.6, 4.8))
for model in data_SD:
    plt.plot(np.log10(model.f), np.log10(model.psd), '-.',
             linewidth=1, label=model.name)
plt.xlabel('log$_{10}$(frequency) [Hz]')
plt.ylabel('log$_{10}$(PSD) [mV$^{2}$/Hz]')
plt.title('PSDs of SD diffusion potential')
plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")  # outside right
plt.savefig('Figures/SD_psd_of_diff_pot', dpi=500)
plt.show()

# =============================================================================
#           Saving SD potential data and SD psd data for later
# =============================================================================
pot_SD_data = {}  # dictionary for potential data
psd_SD_data = {}  # dictionary for psd data
for model in data_SD:
    # potential
    pot_SD_data['t'] = model.t
    pot_SD_data[str(model.name)] = model.exp_decay
    # PSD
    psd_SD_data['f'] = model.f
    psd_SD_data[str(model.name)] = model.psd

df_pot_data = pd.DataFrame(data=pot_SD_data)  # making DataFrame
df_pot_data.to_csv("Data_PSD_other/pot_data_SD.csv", index=False)  # save to file

df_psd_data = pd.DataFrame(data=psd_SD_data)  # making DataFrame
df_psd_data.to_csv("Data_PSD_other/psd_data_SD.csv", index=False)  # save to file
