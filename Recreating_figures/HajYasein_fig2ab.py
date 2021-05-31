import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Reproduce Figure 2 a and b from Hay-Yasein et al.
# Looking at how an exponential decay fit the temporal concentration change

data = pd.read_csv("data_HajYasein2015_fig2ab.csv", header=1)
print(data.columns)
# Columns for Fig2a: X, Y
# Columns for Fig2b: X.1, Y.2

# Figure 2a
time2a = data["X"].values  # time axis
cons2a = data["Y"].values  # K+ concentrations
t_start_decay = 9.767
delta_c_start_decay = 7.955 - cons2a[0]
tau_values = [2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
exp_decay_2a = []
time = np.linspace(t_start_decay, time2a[-1])
for tau in tau_values:
    cons_decay = cons2a[0] + delta_c_start_decay*(np.exp(-(time-t_start_decay)/tau))
    exp_decay_2a.append(cons_decay)

plt.figure()
plt.plot(time2a, cons2a, '.', label='K$^+$ data')
for index, exp_decay in enumerate(exp_decay_2a):
    name = f'$\u03C4$ = {tau_values[index]}'
    plt.plot(time, exp_decay, label=name)
plt.xlabel('Time [s]')
plt.ylabel('Extracellular K$^+$ [mM]')
plt.title('Extracellular K$^+$ from stratum raditum')
plt.legend()
plt.savefig('../Figures/HajYasein_Figure2a.pdf', dpi=500, bbox_inches='tight')
plt.show()

# Figure 2b
time2b = data["X.1"].values  # time axis
cons2b = data["Y.1"].values  # K+ concentrations
t_start_decay = 9.95
delta_c_start_decay = 12.14 - cons2b[0]
tau_values = [2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
exp_decay_2b = []
time = np.linspace(t_start_decay, time2b[-1])
for tau in tau_values:
    cons_decay = cons2b[0] + delta_c_start_decay*(np.exp(-(time-t_start_decay)/tau))
    exp_decay_2b.append(cons_decay)

plt.figure()
plt.plot(time2b, cons2b, '.', label='K$^+$ data')
for index, exp_decay in enumerate(exp_decay_2b):
    name = f'$\u03C4$ = {tau_values[index]}'
    plt.plot(time, exp_decay, label=name)
plt.xlabel('Time [s]')
plt.ylabel('Extracellular K$^+$ [mM]')
plt.title('Extracellular K$^+$ from stratum pyramidale')
plt.legend()
plt.savefig('../Figures/HajYasein_Figure2b.pdf', dpi=500, bbox_inches='tight')
plt.show()
