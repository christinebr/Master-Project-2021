# Master-Project-2021

This repository contains the code used for my Master Thesis.
The thesis marks the end of my study time at NMBU and was finished in the 
spring semester of 2021. 

Overview of the repository:

In **PSD_of_sine_waves.py** I have used a superposition of four sine waves to 
calculate the power spectrum density (PSD) by using the Fast Fourier Transform
(FFT). This is done with two methods: directly with Numpy's fft function and 
with SciPy's ``signal.periodogram`` function. 

**diffusionpotential.py** contains the classes ``Ion`` and 
``DiffusionPotential``. The main class is ``DiffusionPotential`` which is used 
to calculate diffusion potential, the exponential decay of the potential and
the power spectrum density of the potential. 

In **psd_of_lfp_data.py** I have loaded LFP data stored as .mat (because of 
preprocessing in MATLAB) from dataset at CRCNS.org. Then I calculate the 
average PSD and saves it in a .npz file, together with the corresponding
frequency array. Only for data from [CRCNS](https://crcns.org/).

In **plot_psd_data.py** I load the PSD data (which was saved in files by
**psd_of_lfp_data.py**, see above) and plot everything in one figure. 
Only with data from [CRCNS](https://crcns.org/).

In **psd_torbjorn_and_graity.py** I load LFP data from Torbjørn and Graity, 
calculate the mean psd and save to file.

In **plot_psd.py** I plot psd data taken from several figures and from data
of Torbjørn and Graity.

In **diffpot_and_psd.py** I have used scenario 1 (delta_K + delta_Na = 
delta_Cl) to find the initial concentrations. For each concentration data I 
initialize an instance of the ``DiffusionPotential`` class. Each class instance
gets their initial diffusion potential and the exponential decay of that
calculated. Then the PSD of the exponential decaying potential is calculated. 
This file generates two plot: one for the exponentially decaying potential
and one for the PSDs of that potential. At last the exponentially decaying 
diffusion potential, the calculated PSD and corresponding frequency array is 
saved to a .csv file for later use.

In **main_psd_plot.py** I have loaded all files with PSD data and plotted 
everything into one figure.

In **SD_diffpot_and_psd.py** I have used scenario 4 in the case of 
Spreading Depression. The same steps as in **diffpot_and_psd.py** are done 
for this case. 