import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import periodogram

# Trying different time constants and how that affects the PSDs

v0 = 0.2
t_end = 100
N = 10000
fs = N/t_end  # sampling frequency

t = np.linspace(0, t_end, num=N)
tau = [1, 5, 10, 30, 60, 90, 120, 160, 180]
exp_decay = np.zeros(shape=(len(t), len(tau)))
for index, element in enumerate(tau):
    exp_decay[:, index] = v0 * np.exp(-t / element)

tau5 = np.transpose(exp_decay[:, 1])

plt.figure()
plt.plot(t, exp_decay)
plt.title('Exponential decay')
plt.legend(tau)
plt.show()

# PSD
f, pxx = periodogram(np.transpose(exp_decay), fs)

plt.figure()
for index, row in enumerate(pxx):
    if index==0:
        plt.plot(np.log10(f), np.log10(row), '.', label=tau[index])
    else:
        plt.plot(np.log10(f), np.log10(row), label=tau[index])
plt.title('PSD of exponential decay')
plt.legend()
plt.show()

# ========= Concentration decay ============
from diffpot_and_psd import scenario1
t_end = 100
N = 10000
fs = N/t_end

k = [3, 9]
t = np.linspace(0, t_end, num=N)
tau = 5
exp_cons = 3 + (9-3)*np.exp(-t/tau)
plt.figure()
plt.plot(t, exp_cons)
plt.show()

na = []
cl = []
for k_cons in exp_cons:
    c = scenario1(k=k_cons-3, kbase=3, nabase=149)
    na.append(c['Na'][1])
    cl.append(c['Cl'][1])


def henderson(k, na, cl):
    R = 8.3144598
    F = 96485.333
    T = 310
    dk = 1.96e-9
    dna = 1.33e-9
    dcl = 2.03e-9
    kbase = 3*np.ones(len(k))
    nabase = 149*np.ones(len(na))
    clbase = 152*np.ones(len(cl))
    sum1 = dk*(k-kbase)+dna*(na-nabase)-dcl*(cl-clbase)
    sum2 = dk * (k - kbase) + dna * (na - nabase) - dcl * (cl - clbase)
    sum1_ln = dk * kbase + dna * nabase + dcl * clbase
    sum2_ln = dk*k + dna*na + dcl*cl
    return (R*T)/F * (sum1/sum2)*np.log(sum1_ln/sum2_ln)*1000 # mV


k = np.array(exp_cons)
na = np.array(na)
cl = np.array(cl)

pot = henderson(k, na, cl)

plt.figure()
plt.plot(t, pot, label='cons_decay')
plt.ylabel('mV')
plt.xlabel('time')
#plt.show()


# ========= Concentration decay ============
#k = [3, 9]
c = scenario1(k=9-3, kbase=3, nabase=149)
k = np.array(c['K'])
na = np.array(c['Na'])
cl = np.array(c['Cl'])

pot0 = henderson(k[1:], na[1:], cl[1:])

t = np.linspace(0, t_end, num=N)
tau = 5
exp_pot = pot0*np.exp(-t/tau)


plt.plot(t, exp_pot, '--', label='pot_decay')
plt.plot(t, tau5, label='tau=5')
plt.legend()
plt.show()

# PSD
f1, pxx1 = periodogram(pot, fs)
f2, pxx2 = periodogram(exp_pot, fs)

f11, pxx11 = periodogram(abs(pot), fs)
f22, pxx22 = periodogram(abs(exp_pot), fs)

f3, pxx3 = periodogram(tau5, fs)


plt.figure()
plt.plot(np.log10(f1), np.log10(pxx1), label='cons_decay')
plt.plot(np.log10(f2), np.log10(pxx2), '--', label='pot_decay')
plt.plot(np.log10(f3), np.log10(pxx3), '.', label='tau5')
plt.title('PSD of exponential decay')
plt.legend()
plt.show()
