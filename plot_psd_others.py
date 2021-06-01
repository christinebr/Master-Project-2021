import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# This file plot PSD from data collected from figures and some data.


def psd_torbjorn(do_linreg=False, color='cadetblue'):
    # Loading data
    data = np.load("Data_PSD_other/psd_torbjorn.npz")
    # Plotting psd vs. frequency
    log_f = np.log10(data['f'])
    log_psd = np.log10(data['PSD'])
    plt.plot(log_f, log_psd, color=color,
             linewidth=0.5, label='LFP-Torbjørn')
    if do_linreg:  # Linear Regression
        linreg = LinearRegression()
        linreg.fit(log_f.reshape(-1, 1), log_psd.reshape(-1, 1))
        print('Torbjørn\nintercept: ', linreg.intercept_,
              '\nslope: ', linreg.coef_)


def psd_gratiy(do_linreg=False, color='palevioletred'):
    # Loading data
    data = np.load("Data_PSD_other/psd_gratiy.npz")
    # Plotting psd vs. frequency
    log_f = np.log10(data['f'])
    log_psd = np.log10(data['PSD'])
    plt.plot(log_f, log_psd, color=color, label='LFP-Gratiy')
    if do_linreg:  # Linear Regression
        linreg = LinearRegression()
        linreg.fit(log_f[1:].reshape(-1, 1), log_psd[1:].reshape(-1, 1))
        print('Gratiy\nintercept: ', linreg.intercept_,
              '\nslope: ', linreg.coef_)


def psd_from_baranauskas2012(do_linreg=False, color='darkolivegreen'):
    # logX1,logY1,logX2,Y2
    filepath = "Data_PSD_other/psd_Baranbuskas_Fig1C.csv"
    data = pd.read_csv(filepath, usecols=['logX1', 'logY1'])
    log_frequency = np.log10(data['logX1'].values)
    log_psd = np.log10(data['logY1'].values / 1000 ** 2)  # from micro to milli
    plt.plot(log_frequency, log_psd, color=color,
             label='LFP-Baranauskas')
    if do_linreg:  # Linear Regression
        linreg = LinearRegression()
        linreg.fit(log_frequency.reshape(-1, 1), log_psd.reshape(-1, 1))
        print('Baranauskas\nintercept: ', linreg.intercept_,
              '\nslope: ', linreg.coef_)


def psd_from_jankowski2017(do_linreg=False, color='goldenrod'):
    filepath = "Data_PSD_other/psd_Jankowski2017_Fig2F.csv"
    data = pd.read_csv(filepath, usecols=['X', 'Y'])
    log_frequency = np.log10(data['X'].values)
    log_psd = np.log10(data['Y'].values / 1000 ** 2)  # from micro to milli
    plt.plot(log_frequency, log_psd, color=color, label='LFP-Jankowski')
    if do_linreg:  # Linear Regression
        linreg = LinearRegression()
        linreg.fit(log_frequency[:-4].reshape(-1, 1),
                   log_psd[:-4].reshape(-1, 1))
        print('Jankowski\nintercept: ', linreg.intercept_,
              '\nslope: ', linreg.coef_)


def psd_from_miller2009(do_linreg=False, color='sienna'):
    # filepath = "Data_PSD_other/psd_Miller2009_Fig2A.csv"
    filepath = "Data_PSD_other/Miller2009_Fig2A_28.04.csv"
    data = pd.read_csv(filepath, usecols=['X', 'Y'])
    log_frequency = np.log10(data['X'].values)
    log_psd = np.log10(data['Y'].values / 1000 ** 2)  # from micro to milli
    plt.plot(log_frequency, log_psd, color=color, label='LFP-Miller')
    if do_linreg:  # Linear Regression
        linreg = LinearRegression()
        linreg.fit(log_frequency.reshape(-1, 1), log_psd.reshape(-1, 1))
        print('Miller\nintercept: ', linreg.intercept_,
              '\nslope: ', linreg.coef_)


if __name__ == '__main__':
    # Plotting
    plt.figure()

    psd_from_baranauskas2012(do_linreg=True)
    psd_from_jankowski2017(do_linreg=True)
    psd_from_miller2009(do_linreg=True)
    psd_torbjorn(do_linreg=True)
    psd_gratiy(do_linreg=True)

    plt.title('PSDs of LFPs from articles')
    plt.xlabel('log$_{10}$(frequency) [Hz]')
    plt.ylabel('log$_{10}$(PSD) [mV$^{2}$/Hz]')
    plt.xlim([-2, 3.1])
    plt.ylim([-10, 1.2])
    plt.legend(loc="lower left")
    plt.savefig('Figures/psd_from_figures+.pdf', dpi=500, bbox_inches='tight')
    plt.show()
