import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from plot_psd_crcns import get_data_filenames, plot_psd_data
from plot_psd_others import psd_torbjorn, psd_gratiy, psd_from_baranauskas2012

with_diff = False  # True = include diff, False = exclude diff
with_SD = True  # True = include SD, False = exclude SD
zoom = False  # zoomed figure
plt.rc('font', size=13)
plt.figure(figsize=(12, 7))

# CRCNS data
crcns_files = sorted(get_data_filenames(), reverse=True)
index = [4, -4, -1]
colors = ['cornflowerblue', 'gold', 'limegreen', 'darksalmon',
          'maroon', 'darkslategray', 'darkcyan', 'saddlebrown',
          'darkkhaki', 'lightgreen', 'skyblue', 'plum']
abbr = ['A', 'B', 'A', 'B', 'A', 'B', 'C', 'D', 'A', 'B', 'C', 'D']

crcns_files_red = [crcns_files[i] for i in index]
colors_red = [colors[i] for i in index]
abbr_red = [abbr[i] for i in index]
psd_torbjorn()

for file, color, abb in zip(crcns_files_red, colors_red, abbr_red):
    plot_psd_data(file, color, abb)

# other PSD/LFP data
psd_gratiy()
psd_from_baranauskas2012()

# Colors diffusion potentials
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b',
          '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', 'mediumaquamarine',
          'gold', 'lightcoral', 'skyblue', 'palegreen']

# Normal diffusion data
if with_diff:
    diff_data = pd.read_csv("Data_PSD_other/psd_data_normal.csv", index_col='f')
    columns = diff_data.columns
    frequency = diff_data.index.values

    for column, color in zip(columns, colors):
        psd = diff_data[column].values
        plt.plot(np.log10(frequency), np.log10(psd), '--',
                 color=color, label=column)
    plt.title("PSDs of LFPs versus 'normal' diffusion potentials")

# Pathological diffusion data
if with_SD:
    SD_data = pd.read_csv("Data_PSD_other/psd_data_SD.csv", index_col='f')
    columns = SD_data.columns
    frequency = SD_data.index.values

    for column, color in zip(columns, colors):
        psd = SD_data[column].values
        plt.plot(np.log10(frequency), np.log10(psd), '-.',
                 color=color, label=column)
    plt.title("PSDs for LFPs versus 'pathological' diffusion potentials")

# axis labels and legend
plt.xlabel('log$_{10}$(frequency) [Hz]')
plt.ylabel('log$_{10}$(PSD) [mV$^{2}$/Hz]')
if with_diff and zoom:
    plt.xlim([-1.1, 2])
    plt.ylim([-9, -2])
if with_SD and zoom:
    plt.xlim([-1.1, 2])
    plt.ylim([-7, 0])

# plt.legend(loc="lower left", ncol=2)
plt.legend(bbox_to_anchor=(1.04, 1.05), loc="upper left")  # outside right

if with_diff and zoom:
    plt.savefig('Figures/main_REDZOOM_psd_plot.pdf', dpi=500, bbox_inches='tight')
elif with_diff:
    plt.savefig('Figures/main_RED_psd_plot.pdf', dpi=500, bbox_inches='tight')

if with_SD and zoom:
    plt.savefig('Figures/SD_main_REDZOOM_psd_plot.pdf', dpi=500, bbox_inches='tight')
elif with_SD:
    plt.savefig('Figures/SD_main_RED_psd_plot.pdf', dpi=500, bbox_inches='tight')

plt.show()
