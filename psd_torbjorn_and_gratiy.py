import h5py
import numpy as np
from scipy.signal import periodogram

# Load LFP data from Gratiy and Torbjørn, calculating mean PSD and saving
# to file for later.


def calculate_and_save_psd_of_lfp_gratiy():
    """Loading LFP data, calculating mean PSD and saving to file."""
    # Load data
    file_name = 'Data_LFP_other/mouse_1_lfp_trial_avg_3sec.h5'
    h5 = h5py.File(file_name, 'r')
    lfp_off_flash = h5['lfp_off_flash'][...]
    fs = 2500  # sampling rate
    # Calculate PSD
    f, pxx = periodogram(lfp_off_flash, fs)
    # Calculate mean
    psd_off_mean = np.mean(pxx, axis=0)
    # remove data above 100 Hz
    index = np.where(f <= 100)
    f = f[index]
    psd_off_mean = psd_off_mean[index]
    # Save to file
    np.savez('Data_PSD_other/psd_gratiy', f=f, PSD=psd_off_mean)


def calculate_and_save_psd_torbjorn():
    """Loading LFP data, calculating mean PSD and saving to file."""
    # Load data
    lfp = np.load("Data_LFP_other/lfp_run26.npy")[4:-6, :-1]
    samp_rate_lfp = 2000
    # Calculate PSD
    f, pxx = periodogram(lfp, samp_rate_lfp)
    # Calculate mean
    psd_mean = np.mean(pxx, axis=0)
    # remove data below 0.1 Hz and above 100 Hz
    index = np.where((f >= 0.1) & (f <= 100))
    f = f[index]
    psd_mean = psd_mean[index]
    # Save to file
    np.savez('Data_PSD_other/psd_torbjorn', f=f, PSD=psd_mean)


if __name__ == '__main__':
    calculate_and_save_psd_of_lfp_gratiy()
    calculate_and_save_psd_torbjorn()
