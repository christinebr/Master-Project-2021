import os
import numpy as np
import matplotlib.pyplot as plt

# This file load the PSD data (which was saved in files by psd_of_lfp_data.py)
# and plot everything in one figure. Only with data from CRCNS.org.


def get_data_filenames():
    """
    Getting filenames with .npz file extension in 'Data_PSD_crcns' directory.
    The function returns a list of all the filenames.
    """
    directory = "Data_PSD_crcns"
    datafiles = []
    for file in os.listdir(directory):
        if file.endswith(".npz"):
            datafiles.append(file)  # Putting data filename into list
    return datafiles


def plot_psd_data(filename):
    # Loading data
    data = np.load('Data_PSD_crcns/'+filename)
    f = np.array(data['f'][0, :])
    psd = np.array(data['PSD'])
    lw = 0.5
    if 'hc2' in filename or 'pfc2' in filename:
        # remove data below 0.1 Hz
        index = np.where((f >= 0.1) & (f <= 300))
        f = f[index]
        psd = psd[index]
        lw = 0.5
    if 'ac2' in filename:
        # remove data below 0.1 Hz
        index = np.where((f <= 300))
        f = f[index]
        psd = psd[index]
        lw = 1
    if 'bf1' in filename:
        lw = 1

    # Plotting psd vs. frequency
    plt.plot(np.log10(f), np.log10(psd),
             linewidth=lw, label=filename[4:-4])


if __name__ == '__main__':
    data_files = get_data_filenames()

    # Plotting
    plt.figure()
    data_files = sorted(data_files, reverse=True)
    for file in data_files:
        plot_psd_data(file)
    plt.title('PSD of LFP data')
    plt.xlabel('log$_{10}$(frequency) [Hz]')
    plt.ylabel('log$_{10}$(PSD) [mV$^{2}$/Hz]')
    plt.legend(loc="lower left", ncol=2, prop={'size': 8.5})
    plt.savefig('Figures/psd_of_lfp_data.pdf', dpi=500, bbox_inches='tight')
    plt.show()
