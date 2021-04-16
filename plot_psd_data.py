import numpy as np
import matplotlib.pyplot as plt


def plot_psd_data(filename):
    # Loading data
    data = np.load('Data_PSD/'+filename)
    # Plotting psd vs. frequency
    plt.plot(np.log10(data['f'][0, :]), np.log10(data['PSD']),
             linewidth=0.5, label=filename[4:-4])


if __name__ == '__main__':
    # Getting all data file names
    import os
    directory = "Data_PSD"
    data_files = []
    for file in os.listdir(directory):
        if file.endswith(".npz"):
            data_files.append(file)  # Putting data file name into list

    # Plotting
    plt.figure()
    data_files = sorted(data_files, reverse=True)
    for file in data_files:
        plot_psd_data(file)
    plt.title('PSD of LFP data')
    plt.xlabel('log$_{10}$(frequency) [Hz]')
    plt.ylabel('log$_{10}$(PSD) [mV$^{2}$/Hz]')
    plt.legend(loc="lower left", ncol=2)
    # plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")  # outside right
    plt.savefig('Figures/psd_of_lfp_data', dpi=500)
    plt.show()
