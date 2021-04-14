import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import periodogram

# This code demonstrates the use of FFT to calculate the PSD of a simple
# superposition of four sine waves. In addition the periodogram function from
# Scipy's signal package is used to validate the results.

# Defining variables
fs = 15000  # sampling frequency
t = np.linspace(0, 1, fs)  # time vector

# Four sine waves with different frequency
sin1 = np.sin(2*np.pi*1*t)
sin2 = np.sin(2*np.pi*5*t)
sin3 = np.sin(2*np.pi*10*t)
sin4 = np.sin(2*np.pi*30*t)

# Plot of each sine wave
fig = plt.figure()
ax1 = fig.add_subplot(4, 1, 1)
ax1.plot(t, sin1)
ax1.set_title('sin(1*2\u03C0t)')
ax2 = fig.add_subplot(4, 1, 2)
ax2.plot(t, sin2)
ax2.set_title('sin(5*2\u03C0t)')
ax3 = fig.add_subplot(4, 1, 3)
ax3.plot(t, sin3)
ax3.set_title('sin(10*2\u03C0t)')
ax4 = fig.add_subplot(4, 1, 4)
ax4.plot(t, sin4)
ax4.set_title('sin(30*2\u03C0t)')
plt.tight_layout()
plt.savefig('Figures/four_sine_waves', dpi=500)
plt.show()

# Plot of the superposition
v_t = 1*sin1 + 0.5*sin2 + 0.1*sin3 + 0.2*sin4

plt.figure()
plt.plot(t, v_t)
t2 = "v(t) = sin(1*2\u03C0t)+0.5sin(5*2\u03C0t)+0.1sin(10*2\u03C0t)+" \
     "0.2sin(30*2\u03C0t)"
plt.title(t2)
plt.xlabel('t')
plt.ylabel('v(t)')
plt.savefig('Figures/superposition_of_sine_waves', dpi=500)
plt.show()

# Single-sided amplitude spectrum and PSD
N = len(v_t)
fft_ = np.fft.fft(v_t)  # compute the FFT
norm = abs(fft_)/N  # normalize the absolute value of FFT
pos = norm[:N//2]  # using only the positive frequencies
amplitude = 2*pos
PSD = 2*(pos**2)

plt.figure()  # Amplitude
plt.plot(amplitude[:35])  # plot only the first 40
plt.title('Amplitude spectrum of \n'+t2)
plt.xlabel('frequency')
plt.ylabel('amplitude')
plt.savefig('Figures/amplitude_spectrum_sine_waves', dpi=500)
plt.show()

plt.figure()  # PSD
plt.plot(PSD[:35])  # plot only the first 40
plt.title('Power spectrum density of \n'+t2)
plt.xlabel('frequency')
plt.ylabel('power')
plt.savefig('Figures/power_spectrum_sine_waves', dpi=500)
plt.show()

# PSD using periodogram
f, pxx = periodogram(v_t, fs)
plt.figure()
plt.plot(f[:35], pxx[:35])
plt.xlabel('frequency')
plt.ylabel('power')
plt.title('Power spectrum density of\n'+t2+'\n using scipy.signal.periodogram')
plt.show()
