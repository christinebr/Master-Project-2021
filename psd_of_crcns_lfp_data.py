import os
import numpy as np
from scipy.io import loadmat
from scipy.signal import periodogram

# This file load LFP data stored in .mat (MATLAB-file) and calculates a mean
# PSD for the data file. The mean PSD together with the frequency array f is
# stored for later use in .npz files. Only for data from CRCNS.org.


def load_data_calculate_psd_and_save(file_name, lfp_name, fs_name):
    """
    Loading the LFP data (and the sampling frequency) and calculating PSD with
    the periodogram function for each channel/row in the data. Then averaging
    to get a mean PSD estimate and saving it together with the frequency
    array in a file.
    """
    data = loadmat('Data_LFP_crcns/'+file_name)[lfp_name]  # loading LFP data
    fs = loadmat('Data_LFP_crcns/'+file_name)[fs_name]  # sampling rate

    psd = []
    f = None
    for row in data:
        f, pxx = periodogram(row, fs)  # PSD for one row of LFP data
        psd.append(pxx)

    mean_psd = np.mean(np.array(psd), axis=0)  # mean PSD over all rows

    # Save to file
    np.savez('Data_PSD_crcns/psd_' + file_name[:-4], f=f, PSD=mean_psd)


if __name__ == '__main__':
    # Getting all data file names
    directory = "Data_LFP_crcns"
    data_files = []
    for file in os.listdir(directory):
        if file.endswith(".mat"):
            # Putting data file name into list
            data_files.append(file)

    # Using function above to load data, calculate PDS and save to file
    counter = 1
    for filename in data_files:
        print(counter, filename)
        counter += 1
        if 'ac2' in filename:
            load_data_calculate_psd_and_save(filename, 'all_sweeps_lfp',
                                             'sample_per_second')
        elif 'hc2' in filename:
            load_data_calculate_psd_and_save(filename, 'volt_lfp', 'fs')

        elif 'bf1' in filename:
            load_data_calculate_psd_and_save(filename, 'LFP_data', 'fs')

        elif 'pfc2' in filename:
            if 'ca1' in filename:
                load_data_calculate_psd_and_save(filename, 'volt_ca1', 'fs')
            else:
                load_data_calculate_psd_and_save(filename, 'volt_pfc', 'fs')
