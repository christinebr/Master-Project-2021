# Master-Project-2021

This repository contains the code used for my Master Thesis.
The thesis marks the end of my study time at NMBU and was finished in the 
spring semester of 2021. 

<ins>Overview of the files in this repository:</ins>

In **PSD_of_sine_waves.py** I have used a superposition of four sine waves to 
calculate the power spectrum density (PSD) by using the Fast Fourier Transform
(FFT). This is done with two methods: directly with Numpy's fft function and 
with SciPy's ``signal.periodogram`` function. 

**diffusionpotential.py** contains the classes ``Ion`` and 
``DiffusionPotential``. The main class is ``DiffusionPotential`` which is used 
to calculate diffusion potential, the exponential decay of the potential and
the power spectrum density of the potential. 

In **comparing_equations_and_scenarios.py** I have used scenario 1-4 for
some concentration differences of extracellular K+ to calculate Na+ and Cl-. 
Then I have estimated the diffusion potential with the Goldman equation, the
Henderson equation and the approximated equation. I have also estimated PSDs 
to compare the four scenarios. The functions for scenario 2 and 3 is placed 
in **scenario.py**.

In **diffpot_and_psd.py** I have used scenario 1 (delta_K + delta_Na = 
delta_Cl) to find the initial concentrations. For each concentration data I 
initialize an instance of the ``DiffusionPotential`` class. Each class instance
gets their initial diffusion potential and the exponential decay of that
calculated. Then the PSD of the exponential decaying potential is calculated. 
This file generates two plot: one for the exponentially decaying potential
and one for the PSDs of that potential. At last the exponentially decaying 
diffusion potential, the calculated PSD and corresponding frequency array is 
saved to a .csv file for later use. All the same steps are done for the 
'pathological' cases, where I used scenario 4. See **SD_diffpot_and_psd.py**.


In **psd_of_crcns_lfp_data.py** I have loaded LFP data stored as .mat (because of 
preprocessing in MATLAB) from dataset at CRCNS.org. Then I calculate the 
average PSD and saves it in a .npz file, together with the corresponding
frequency array. Only for data from [CRCNS](https://crcns.org/).

In **plot_psd_crcns.py** I load the PSD data (which was saved in files by
**psd_of_lfp_data.py**, see above) and plot everything in one figure. 
Only with data from [CRCNS](https://crcns.org/).

In **psd_torbjorn_and_graity.py** I load LFP data from Torbjørn and Graity, 
calculate the mean psd and save to file.

In **torbjorn.py** and **graity.py** I compare SciPy's signal.periodiogram 
function and the PSD-formula. I use the LFP data and calculate the power 
spectrum density (PSD) with both method. The results are plotted in the same 
figure.

In **plot_psd_others.py** I plot psd data taken from several figures 
(Baranauskas, Jankowski, and Miller) and from LFP data from Torbjørn and
Graity.

The **LFP_PSDs_chosed.py** file plot all PSDs of LFPs with the chosen PSDs in
color and the rest in grayscale.

In **main_psd_plot.py** I have loaded all files with PSD data and plotted 
everything into one figure. A reduced version of this figure is produced in 
**main_psd_plot_reduced.py** where only some of the PSD data is plotted 
together with the PSDs of diffusion potentials.


<ins>Overview of directories in this repository:</ins>

**Data_PSD_crcns** contain the estimated PSD for CRCNS data sets

**Data_PSD_other** contain PSD calculated from two data sets, and from 
figures in articles

**Recreating_figures** contain concentration data from
figures and .py files for recreating these. 