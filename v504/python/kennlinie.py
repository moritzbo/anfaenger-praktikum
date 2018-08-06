import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy import optimize
import scipy.constants as const
from scipy.stats import sem

v20, a20 = np.genfromtxt('python/2a.txt', unpack=True)
v21, a21 = np.genfromtxt('python/21a.txt', unpack=True)
v22, a22, a23, a24 = np.genfromtxt('python/22-23-24a.txt', unpack=True)
plt.plot(v20, a20, 'x', label=r'$\SI{2.0}{\ampere}$')
plt.plot(v21, a21, 'x', label=r'$\SI{2.1}{\ampere}$')
plt.plot(v22, a22, 'x', label=r'$\SI{2.2}{\ampere}$')
plt.plot(v22, a23, 'x', label=r'$\SI{2.3}{\ampere}$')
plt.plot(v22, a24, 'x', label=r'$\SI{2.4}{\ampere}$')
plt.xlim(0,200)
plt.ylim(0, 1.6)
plt.xlabel(r'$\symup{U}\;/\;\si{\volt}$')
plt.ylabel(r'$\symup{I}\;/\;\si{\milli\ampere}$')
plt.grid()
plt.legend()
plt.savefig('build/kennlinie.pdf')
plt.clf()

nwl = 0.9 #-1W
eta = 0.28
flaeche = 0.35*10**(-4) #m^2
stbol = const.Stefan_Boltzmann #W/m^2K^4
charge = const.elementary_charge
mass = const.electron_mass
kbol = const.Boltzmann
hplanck = const.Planck
print('charge',charge)
print('mass',mass)
print('stbol',stbol)
print('kbol',kbol)
print('hplanck',hplanck)
nenner=flaeche*eta*stbol
ih = [2.0, 2.1, 2.2, 2.3, 2.4]
vh = [4.35, 4.6, 4.95, 5.4, 5.65]
si = [0.095, 0.2, 0.45, 0.82, 1.5]
th = np.ones(len(ih))
phi = np.ones(len(ih))
for i in range(5):
    th[i] = ((ih[i]*vh[i]-nwl)/(nenner))**(1/4)
    phi[i] = -(kbol*th[i])/charge*np.log((si[i]*hplanck**3)/(4*np.pi*flaeche*charge*mass*kbol**2*(th[i])**2))
np.savetxt('build/kennlinientemperatur.txt', np.column_stack([vh, ih, si, th]),header='vh, ih, si, th')
print(np.column_stack([phi]))
print(np.mean(phi))
print(sem(phi))

# Abspeichern der Kennliniendaten
def umspeichern(a):
    i = 0
    b = np.zeros(17)
    while i < len(a):
        b[i] = a[i]
        i = i + 1
    return b

v20n = umspeichern(v20)
v22n = umspeichern(v22)
a20n = umspeichern(a20)
a22n = umspeichern(a22)
a23n = umspeichern(a23)
a24n = umspeichern(a24)
np.savetxt('build/kennliniendaten.txt',
np.column_stack([v20n, a20n, v21, a21, v22n, a22n, a23n, a24n]),
header='v20n, a20n, v21, a21, v22n, a22n, a23n, a24n')
