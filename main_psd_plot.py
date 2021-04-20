import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from plot_psd_data import get_data_filenames, plot_psd_data
from plot_psd import psd_torbjorn, psd_graity, psd_from_miller2009, \
    psd_from_milstein2009, psd_from_baranauskas2012, psd_from_jankowski2017

with_SD = True  # True = include SD, False = exclude SD

plt.figure(figsize=(12, 7))

# CRCNS data
crcns_files = sorted(get_data_filenames(), reverse=True)

for file in crcns_files:
    plot_psd_data(file)

# other PSD/LFP data
psd_torbjorn()
psd_graity()
psd_from_miller2009()
psd_from_milstein2009()
psd_from_baranauskas2012()
psd_from_jankowski2017()

# Diffusion data
diff_data = pd.read_csv("Data_PSD_other/psd_data_normal.csv", index_col='f')
columns = diff_data.columns
frequency = diff_data.index.values

for col in columns:
    psd = diff_data[col].values
    plt.plot(np.log10(frequency), np.log10(psd), '--', label=col)

# Spreading depression
if with_SD:
    SD_data = pd.read_csv("Data_PSD_other/psd_data_SD.csv", index_col='f')
    columns = SD_data.columns
    frequency = SD_data.index.values

    for col in columns:
        psd = SD_data[col].values
        plt.plot(np.log10(frequency), np.log10(psd), '-.', label=col)

# Title, label and legend
plt.title('PSD of diffusion potential, crcns data and other data')
plt.xlabel('log$_{10}$(frequency) [Hz]')
plt.ylabel('log$_{10}$(PSD) [mV$^{2}$/Hz]')
# plt.xlim([-1, 2])
# plt.ylim([-10, 1])
# plt.legend(loc="lower left", ncol=2)
plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left", ncol=2)  # outside right

if with_SD:
    plt.savefig('Figures/SD_main_psd_plot', dpi=500, bbox_inches='tight')
else:
    plt.savefig('Figures/main_psd_plot', dpi=500, bbox_inches='tight')

plt.show()
