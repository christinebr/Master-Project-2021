import matplotlib.pyplot as plt
from plot_psd_crcns import get_data_filenames, plot_psd_data
from plot_psd_others import psd_torbjorn, psd_graity, psd_from_miller2009, \
    psd_from_baranauskas2012, psd_from_jankowski2017

# This file plots the chosen PSD of LFPs in color and the others in grayscale

plt.rc('font', size=13)
plt.figure(figsize=(12, 7))
psd_torbjorn()
# CRCNS data
crcns_files = sorted(get_data_filenames(), reverse=True)
colors = ['grey', 'grey', 'darkgrey', 'darkgrey',
          'maroon', 'lightgrey', 'lightgrey', 'lightgrey',
          'darkkhaki', 'grey', 'grey', 'plum']
abbr = ['A', 'B', 'A', 'B', 'A', 'B', 'C', 'D', 'A', 'B', 'C', 'D']
for file, color, abb in zip(crcns_files, colors, abbr):
    plot_psd_data(file, color, abb)

# other PSD/LFP data
psd_graity()
psd_from_miller2009(color='grey')
psd_from_baranauskas2012()
psd_from_jankowski2017(color='grey')

plt.title('All PSDs of LFP data')
# axis labels and legend
plt.xlabel('log$_{10}$(frequency) [Hz]')
plt.ylabel('log$_{10}$(PSD) [mV$^{2}$/Hz]')
plt.legend(bbox_to_anchor=(1.03, 1.0), loc="upper left")  # outside right

plt.savefig('Figures/PSD_LFP_chosed.pdf', dpi=500, bbox_inches='tight')

plt.show()
