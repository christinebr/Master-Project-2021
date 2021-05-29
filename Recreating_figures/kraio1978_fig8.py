import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read in data, interpolate and plot (recreate) Figure 8 from Kraig1978
# Also print concentrations at t = 0, t = 1min and Δc

data = pd.read_csv("data_kraig1978_fig8.csv", header=1)
# cl data,,na data,,k data,,a data,
# print(data.columns)
# Index(['X', 'Y', 'X.1', 'Y.1', 'X.2', 'Y.2', 'X.3', 'Y.3'], dtype='object')
# X is time [min] and Y is concentration [mM]

# Sorting data in time arrays and concentration arrays
list_of_t = []
list_of_c = []
for col in data.columns:
    if "Y.2" in col:
        d = data[col].values + 2.3  # to get correct baseline for K+
    else:
        d = data[col].values
    new_d = d[~(np.isnan(d))]  # remove NaN

    if "X" in col:
        list_of_t.append(new_d)  # X = time
    else:
        list_of_c.append(new_d)  # Y = concentration

# Interpolating
time = np.linspace(0, 3.7, num=100)  # create common time axis
interpolate = [[], [], [], []]  # to store interpolated values is
for index, t, c in zip(range(4), list_of_t, list_of_c):
    t_sort = t.argsort()  # sort index after increasing time
    sorted_t = t[t_sort]
    sorted_c = c[t_sort]
    interpolate[index] = np.interp(time, sorted_t, sorted_c)

# Calculation of A-
calculated_A = interpolate[2] + interpolate[1] - interpolate[0]

# Plotting
plt.rc('font', size=13)
plt.figure()
for i in interpolate[:-1]:
    plt.plot(time, i)
plt.plot(time, calculated_A)
plt.legend(["Cl", "Na", "K", "A (calculated)"])
plt.title("Concentrations during spreading depression")
plt.xlabel('time [min]')
plt.ylabel('ECS concentration [mM]')
plt.savefig('../Figures/kraigfig8.pdf', dpi=500, bbox_inches='tight')
plt.show()

plt.figure()
el_neutral = interpolate[2] + interpolate[1] - (interpolate[0] + calculated_A)
plt.plot(time, el_neutral)
plt.title("Electroneutrality: K + Na - (Cl + A)")
plt.xlabel('time [min}')
plt.ylabel('')
plt.savefig('../Figures/kraigfig8_elneu.pdf', dpi=500, bbox_inches='tight')
plt.show()

# Printing concentrations of Cl, Na, K and A at certain times
t1 = np.where(abs(time - 1.00) < 0.01)[0][0]  # index to time = 1 min
print("Ion     t = 0             t = 1 min          Δc")
for i, name in zip(interpolate, ["Cl", "Na", "K "]):
    change = i[0] - i[t1]
    print(name, i[0], i[t1], change)
change = calculated_A[0] - calculated_A[t1]
print("A ", calculated_A[0], calculated_A[t1], change)
