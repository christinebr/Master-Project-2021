# Master-Project-2021

This repository contains the code used for my Master Thesis.
The thesis marks the end of my study time at NMBU and was finished in the 
spring semester of 2021. 

Overview of the repository:

In **PSD_of_sine_waves.py** I have used a superposition of four sine waves to 
calculate the power spectrum density (PSD) by using the Fast Fourier Transform
(FFT). This is done with two methods: directly with Numpy's fft function and 
with SciPy's ``signal.periodogram`` function. 

In **diffusionpotential.py** contains the classes ``Ion`` and 
``DiffusionPotential``. The main class is ``DiffusionPotential`` which is used 
to calculate diffusion potential, the exponential decay of the potential and
the power spectrum density of the potential. 
