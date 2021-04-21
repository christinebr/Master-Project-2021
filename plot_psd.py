import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# This file plot PSD from data collected from figures and some data.


def psd_torbjorn():
    # Loading data
    data = np.load("Data_PSD_other/psd_torbjorn.npz")
    # Plotting psd vs. frequency
    plt.plot(np.log10(data['f']), np.log10(data['PSD']),
             linewidth=0.5, label='LFP-Torbjørn')


def psd_graity():
    # Loading data
    data = np.load("Data_PSD_other/psd_graity.npz")
    # Plotting psd vs. frequency
    plt.plot(np.log10(data['f']), np.log10(data['PSD']), label='LFP-Graity')


def psd_from_baranauskas2012():
    # logX1,logY1,logX2,Y2
    filepath = "Data_PSD_other/psd_Baranbuskas_Fig1C.csv"
    data = pd.read_csv(filepath, usecols=['logX1', 'logY1'])
    frequency = data['logX1'].values
    psd = data['logY1'].values / 1000 ** 2  # from micro to milli
    plt.plot(np.log10(frequency), np.log10(psd), label='LFP-Baranauskas2012')


def psd_from_milstein2009():
    # X,Y
    filepath = "Data_PSD_other/psd_Milstein2009_Fig1.csv"
    data = pd.read_csv(filepath, usecols=['X', 'Y'])
    frequency = data['X'].values
    psd = data['Y'].values / 1000 ** 2  # from micro to milli
    plt.plot(np.log10(frequency), np.log10(psd), label='LFP-Milstein2009')


def psd_from_jankowski2017():
    filepath = "Data_PSD_other/psd_Jankowski2017_Fig2F.csv"
    data = pd.read_csv(filepath, usecols=['X', 'Y'])
    frequency = data['X'].values
    psd = data['Y'].values / 1000 ** 2  # from micro to milli
    plt.plot(np.log10(frequency), np.log10(psd), label='LFP-Jankowski2017')


def psd_from_miller2009():
    filepath = "Data_PSD_other/psd_Miller2009_Fig2A.csv"
    data = pd.read_csv(filepath, usecols=['X', 'Y'])
    frequency = data['X'].values
    psd = data['Y'].values / 1000 ** 2  # from micro to milli
    plt.plot(np.log10(frequency), np.log10(psd), label='LFP-Miller2009')


if __name__ == '__main__':
    # Plotting
    plt.figure()

    psd_torbjorn()
    psd_graity()
    psd_from_baranauskas2012()
    psd_from_milstein2009()
    psd_from_jankowski2017()
    psd_from_miller2009()

    plt.title('PSDs of LFPs')
    plt.xlabel('log$_{10}$(frequency) [Hz]')
    plt.ylabel('log$_{10}$(PSD) [mV$^{2}$/Hz]')
    plt.legend(loc="lower left", ncol=2)
    plt.savefig('Figures/psd_from_figures+', dpi=500)
    plt.show()
