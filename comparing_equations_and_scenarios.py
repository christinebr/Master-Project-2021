from diffusionpotential import DiffusionPotential
from diffpot_and_psd import scenario1
from scenario import scenario2, scenario3
from SD_diffpot_and_psd import scenario4
import numpy as np
import matplotlib.pyplot as plt

# Calculating the potential with the Goldman equation, the Henderson equation
# and the approximated sigma equation (for scenario 1-4)
# In addition, estimating and plotting PSDs for scenario 1-4

potassium = [2, 4, 6, 9]  # delta K difference from baseline of 3 mM
scenario_functions = [scenario1, scenario2, scenario3, scenario4]
colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red']
line = ['-', '--', '-.', ':']  # line styles for plotting

plot_all_cases = False
if plot_all_cases:
    plt.figure(figsize=(12, 7))
else:
    plt.figure()

for scen, number in zip(scenario_functions, ["1", "2", "3", "4"]):
    table = np.zeros(shape=(4, 4))
    for index, k in enumerate(potassium):
        c = scen(k=k, kbase=3.0, nabase=149.0)
        model = DiffusionPotential(conc=c, tau=5, delta_t=0.01, t_end=100,
                                   name='K+ = +'+str(k))
        model.calculate_everything(henderson=True)

        # Add potential estimates to table
        table[0, index] = k
        table[1, index] = model.goldman
        table[2, index] = model.henderson
        table[3, index] = model.delta_phi

        # Plotting PSDs
        if plot_all_cases:
            plt.plot(np.log10(model.f), np.log10(model.psd),
                     line[int(number)-1], color=colors[index],
                     label='Scenario ' + number + ' ' + model.name)
        elif k == 4:
            plt.plot(np.log10(model.f), np.log10(model.psd),
                     label='Scenario ' + number)
    print("sceario"+number)
    print(table)

# Legend, title, axis and saving the figure
if plot_all_cases:
    plt.legend(bbox_to_anchor=(1.04, 1.05), loc="upper left")
    plt.title('PSD - Comparing scenarios, $\u03C4$=5 s')
    plt.xlabel('log$_{10}$(frequency) [Hz]')
    plt.ylabel('log$_{10}$(PSD) [mV$^{2}$/Hz]')
    plt.savefig('Figures/PSD_comparing_scenarios.pdf',
                dpi=500, bbox_inches='tight')

else:
    plt.legend()
    plt.title('PSD - Comparing scenarios, $\u03C4$=5 s, K = +4')
    plt.xlabel('log$_{10}$(frequency) [Hz]')
    plt.ylabel('log$_{10}$(PSD) [mV$^{2}$/Hz]')
    plt.savefig('Figures/PSD_comparing_scenariosk2.pdf',
                dpi=500, bbox_inches='tight')
plt.show()

potassium_SD = [20, 30, 40, 50]
table = np.zeros(shape=(4, 4))

plt.figure()
for index, k in enumerate(potassium_SD):
    c = scenario4(k=k, kbase=3.0, nabase=149.0)
    model = DiffusionPotential(conc=c, tau=5, delta_t=0.01, t_end=100,
                               name='K+ = +'+str(k))
    model.calculate_everything()

    table[0, index] = k
    table[1, index] = model.goldman
    table[2, index] = model.henderson
    table[3, index] = model.delta_phi

    plt.plot(np.log10(model.f), np.log10(model.psd),
             label='Scenario 4'+' ' + model.name)
print("scenario 4")
print(table)

plt.title('PSD - Scenario 4, $\u03C4$=5 s')
plt.xlabel('log$_{10}$(frequency) [Hz]')
plt.ylabel('log$_{10}$(PSD) [mV$^{2}$/Hz]')
plt.legend()
plt.show()
