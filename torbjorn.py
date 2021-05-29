import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import periodogram

# In this file I calculate the PSD of Torbjørn's LFP data using SciPy's
# signal.periodogram function, and by using the formula for PSD.
# The result of both method are plotted in the same figure. The lines
# overlap which indicate that the two methods give the same result


def psd_with_periodogramn():
    """Calculate and plot mean psd with periodogram function"""
    # Load data
    lfp = np.load("Data_LFP_other/lfp_run26.npy")[4:-6, :-1]
    samp_rate_lfp = 2000  # sample rate
    # Calculate psd for each channel
    f, pxx = periodogram(lfp, samp_rate_lfp)
    # Calculate mean
    psd_mean = np.mean(pxx, axis=0)
    # Plot
    plt.plot(np.log10(f), np.log10(psd_mean),
             linewidth=0.5, label='periodogram')


def psd_with_formula():
    """Calculate and plot mean psd with formula"""
    # Load data
    lfp = np.load("Data_LFP_other/lfp_run26.npy")[4:-6, :-1]

    n_points = lfp.shape[1]  # number of points
    samp_rate_lfp = 2000  # sample rate
    dt = 1 / samp_rate_lfp  # delta t
    df = samp_rate_lfp/n_points  # delta f

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
    plt.title('PSD of LFP data from Torbjørn')

    psd_with_periodogramn()
    psd_with_formula()

    plt.xlabel('log$_{10}$(frequency) [Hz]')
    plt.ylabel('log$_{10}$(PSD) [mV$^{2}$/Hz]')
    plt.legend()
    plt.show()
