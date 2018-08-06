import numpy as np
from scipy.stats import sem
import matplotlib.pyplot as plt

x = np.ones(10)
dv, ve, u, ue = np.genfromtxt('python/saegezahnanalyse.txt', unpack=True)

for i in range(10):
    x[i] = u[i]*(1+i)*np.pi/2
e = x.mean()
n = np.ones(10)
for m in range(10):
    n[m] = 2*e/(np.pi*(m+1))
f = 100-100*u/n
ea = np.ones(10)
ea *= e
ma = np.ones(10)
ma *= sem(x)

plt.xlabel('ν')
plt.ylabel('Amplitude')
plt.xlim(0, 10)
plt.ylim(0, 232)
t = np.arange(1, 11)
plt.plot(t, u, 'gx', label="Messwerte")
plt.plot(t, n, 'yx', label="Theoriewerte")

plt.errorbar(t, u, yerr=ue, fmt='|')

plt.legend()
plt.grid()
plt.show()
plt.savefig('build/saegezahnanalyse.pdf')

np.savetxt('build/saegezahn.txt', np.column_stack([n, f, ea, ma]), header="Theoriewerte, Fehler/Abweichung")
