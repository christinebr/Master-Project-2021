import h5py
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import periodogram

# Here I calculated the PSD of Gratiy's LFP data using SciPy's
# signal.periodogram function, and by using the formula for PSD.
# The result of both method are plotted in the same figure. The lines
# overlap which indicate that the two methods give the same result


def psd_periodogram():
    file_name = 'Data_LFP_other/mouse_1_lfp_trial_avg_3sec.h5'
    h5 = h5py.File(file_name, 'r')
    lfp_off_flash = h5['lfp_off_flash'][...]

    fs = 2500  # sampling rate

    f, pxx = periodogram(lfp_off_flash, fs)

    # Calculate mean
    psd_off_mean = np.mean(pxx, axis=0)

    # Plotting
    plt.plot(np.log10(f), np.log10(psd_off_mean),
             linewidth=0.5, label='periodogram')


def psd_formula():
    """Calculate and plot mean psd with formula"""
    # Load data
    file_name = 'Data_LFP_other/mouse_1_lfp_trial_avg_3sec.h5'
    h5 = h5py.File(file_name, 'r')
    lfp = h5['lfp_off_flash'][...]

    n_points = lfp.shape[1]  # number of points
    fs = 2500  # sampling rate
    dt = 1 / fs  # delta t
    df = fs/n_points  # delta f

    # Getting the sample frequencies of the Discrete Fourier Transform (DFT)
    f_dft = np.fft.fftfreq(n_points, d=dt)
    freq = f_dft[:n_points//2]  # only positive frequencies (one-sided)

    # Compute the DFT of lfp by using the Fast Fourier Transform (FFT)
    fft = np.abs(np.fft.fft(lfp))/n_points
    # Power spectrum (PS)
    ps = 2*(fft[:, :n_points//2]**2)  # only positive frequencies (one-sided)
    # Power spectrum density (PSD)
    psd = ps / df
    # Computing the mean psd
    psd_mean = np.mean(psd, axis=0)
    # Plotting
    plt.plot(np.log10(freq), np.log10(psd_mean),
             linewidth=0.5, label='formula')


if __name__ == '__main__':
    plt.figure()
    plt.title('PSD of LFP data from Gratiy')

    psd_periodogram()
    psd_formula()

    plt.xlabel('log$_{10}$(frequency) [Hz]')
    plt.ylabel('log$_{10}$(PSD) [mV$^{2}$/Hz]')
    plt.legend()
    plt.show()
