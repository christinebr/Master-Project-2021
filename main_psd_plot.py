import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from plot_psd_crcns import get_data_filenames, plot_psd_data
from plot_psd_others import psd_torbjorn, psd_gratiy, psd_from_miller2009, \
    psd_from_baranauskas2012, psd_from_jankowski2017

# This file plots PSD from all cases in one figure

with_diff = True  # True = include diff, False = exclude diff
with_SD = False  # True = include SD, False = exclude SD
plt.rc('font', size=13)
plt.figure(figsize=(14, 10))
psd_torbjorn()
# CRCNS data
crcns_files = sorted(get_data_filenames(), reverse=True)
colors = ['cornflowerblue', 'gold', 'limegreen', 'darksalmon',
          'maroon', 'darkslategray', 'darkcyan', 'saddlebrown',
          'darkkhaki', 'lightgreen', 'skyblue', 'plum']
abbr = ['A', 'B', 'A', 'B', 'A', 'B', 'C', 'D', 'A', 'B', 'C', 'D']
for file, color, abb in zip(crcns_files, colors, abbr):
    plot_psd_data(file, color, abb)

# other PSD/LFP data
psd_gratiy()
psd_from_miller2009()
psd_from_baranauskas2012()
psd_from_jankowski2017()

# Colors diffusion potentials
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b',
          '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', 'mediumaquamarine',
          'gold', 'lightcoral', 'skyblue', 'palegreen']

# Normal data
if with_diff:
    diff_data = pd.read_csv("Data_PSD_other/psd_data_normal.csv", index_col='f')
    columns = diff_data.columns
    frequency = diff_data.index.values

    for col, color in zip(columns, colors):
        psd = diff_data[col].values
        plt.plot(np.log10(frequency), np.log10(psd), '--',
                 color=color, label=col)

    plt.title("PSDs of 'normal' diffusion potentials, CRCNS data sets and"
              " other LFP data")

# Spreading depression
if with_SD:
    SD_data = pd.read_csv("Data_PSD_other/psd_data_SD.csv", index_col='f')
    columns = SD_data.columns
    frequency = SD_data.index.values

    for col, color in zip(columns, colors):
        psd = SD_data[col].values
        plt.plot(np.log10(frequency), np.log10(psd), '-.',
                 color=color, label=col)

    plt.title("PSD of 'pathological' diffusion potentials, CRCNS data sets"
              " and other LFP data")
# axis labels and legend
plt.xlabel('log$_{10}$(frequency) [Hz]')
plt.ylabel('log$_{10}$(PSD) [mV$^{2}$/Hz]')
# plt.xlim([-1, 2])
# plt.ylim([-10, 1])
# plt.legend(loc="lower left", ncol=2)
# plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left", ncol=2)  # outside right
plt.legend(bbox_to_anchor=(0.5, -0.08), loc="upper center", ncol=5)  # outside right

if with_diff:
    plt.savefig('Figures/main_psd_plot.pdf', dpi=500, bbox_inches='tight')
if with_SD:
    plt.savefig('Figures/SD_main_psd_plot.pdf', dpi=500, bbox_inches='tight')

plt.show()
