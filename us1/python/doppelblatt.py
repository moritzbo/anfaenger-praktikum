import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
import uncertainties.unumpy as unp
from scipy import optimize
import scipy.constants as const
from scipy.stats import sem

t, u, hf, tgc = np.genfromtxt('python/daten/programm/doppelblattzylindermessung.txt', unpack=True)

tpeaks = [0.40, 30.60, 43.80, 57.10]
length = len(tpeaks)
hpeaks = np.ones(length)
hdiff = np.ones(length)
c = 2730
i = 0
while i < length:
    tpeaks[i] = tpeaks[i]*10**(-6)
    hpeaks[i] = c*tpeaks[i]/2
    i += 1
i = 1
while i < length:
    hdiff[i] = abs(hpeaks[i]-hpeaks[i-1])
    i += 1

np.savetxt('build/doppelblatt.txt',
        np.column_stack([tpeaks, hpeaks, hdiff]),
        header='tpeaks, hpeaks, hdiff')

plt.plot(t, u, 'k.', markersize=3, label='Messwerte')
plt.xlabel(r'$t\;/\;\si{\micro\second}$')
plt.ylabel(r'$U\;/\;\si{\volt}$')
plt.xlim(-1, 101)
plt.ylim(-0.01, 1.5)
plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig('build/doppelblatt.pdf')
