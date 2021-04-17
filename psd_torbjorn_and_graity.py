import h5py
import numpy as np
from scipy.signal import periodogram

# Load LFP data from Graity and Torbjørn, calculating mean PSD and saving
# to file for later.


def calculate_and_save_psd_of_lfp_graity():
    """
    Function modified from electrodiffusion.py PSD_of_LFP
    Removed lines that were commented out and things that were not used
    """
    file_name = 'Data_LFP_other/mouse_1_lfp_trial_avg_3sec.h5'
    h5 = h5py.File(file_name, 'r')
    lfp_off_flash = h5['lfp_off_flash'][...]
    z = h5['zdepth'][...]
    time = h5['time'][...]

    fs = 2500  # sampling rate

    psd_off = np.zeros((len(z), len(time) // 2 + 1))
    f = None
    for index, data_ch in enumerate(lfp_off_flash):
        f, pxx = periodogram(data_ch, fs)
        psd_off[index, :] = pxx
    # Calculate mean
    psd_off_mean = np.mean(psd_off, axis=0)
    # Save to file
    np.savez('Data_PSD_other/psd_graity', f=f, PSD=psd_off_mean)


def calculate_and_save_psd_torbjorn():
    """Loading LFP data, calculating mean PSD and saving to file."""
    lfp = np.load("Data_LFP_other/lfp_run26.npy")[4:-6, :-1]
    samp_rate_lfp = 2000
    f, pxx = periodogram(lfp, samp_rate_lfp)
    # Calculate mean
    psd_mean = np.mean(pxx, axis=0)
    # Save to file
    np.savez('Data_PSD_other/psd_torbjorn', f=f, PSD=psd_mean)


if __name__ == '__main__':
    calculate_and_save_psd_of_lfp_graity()
    calculate_and_save_psd_torbjorn()
