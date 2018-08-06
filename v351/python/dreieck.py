import numpy as np
from scipy.stats import sem
import matplotlib.pyplot as plt

x = np.ones(10)
dv, ve, u, ue = np.genfromtxt('python/dreieckanalyse.txt', unpack=True)

for i in range(10):
    x[i] = (u[i]*(2*i+1)**2*np.pi**2)/8  # Grundamplitude ausrechnen
e = x.mean()
n = np.ones(10)
for m in range(10):
    n[m] = 8*e/(np.pi**2*(2*m+1)**2)  # Theoriewerte berechnen
f = 100-100*u/n
ea = np.ones(10)
ea *= e
ma = np.ones(10)
ma *= sem(x)

plt.xlabel('ν')
plt.ylabel('Amplitude')
plt.xlim(1, 19)
plt.ylim(0, 260)
plt.xticks([1, 3, 5, 7, 9, 11, 13, 15, 17, 19])
tn = np.arange(1, 20)
t = tn[tn % 2 == 1]
plt.plot(t, u, 'gx', label="Messwerte")
plt.plot(t, n, 'yx', label="Theoriewerte")

plt.errorbar(t, u, yerr=ue, fmt='|')

plt.legend()
plt.grid()
plt.show()
plt.savefig('build/dreieckanalyse.pdf')

np.savetxt('build/dreieck.txt', np.column_stack([n, f, ea, ma]), header="Theoriewerte, Fehler/Abweichung")
