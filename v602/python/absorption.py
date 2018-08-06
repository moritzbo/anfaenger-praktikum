import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as const
from scipy import optimize
from uncertainties import ufloat

ordnung = [30,35,38,40,80,80]
ordnung2 = [900, 1225, 1444, 1600, 6400, 6400]
anzahl = len(ordnung)
phik = [37, 26.2, 22, 19.5, 25.2, 29.6]
thetak = np.ones(anzahl)
ek = np.ones(anzahl)
sigmak = np.ones(anzahl)

h = const.Planck
c = const.speed_of_light
d = 201.4*10**(-12)
q = const.elementary_charge
rhyd = 13.6
a = 7.2973525664*10**(-3)

def energie(phi):
    phi = phi * np.pi/180
    return (h*c)/(2*d*q*np.sin(phi/2))

for i in range(anzahl):
    thetak[i] = phik[i]/2
    ek[i] = energie(phik[i])
    sigmak[i] = ordnung[i]-np.sqrt(ek[i]/rhyd)
i = -1
deltaE = ek[-2]-ek[-1]
DeltaE = 14215 - 12290
sigmak[i-1] = ordnung[i] - np.sqrt(4/a * np.sqrt(deltaE/rhyd) - 5*deltaE/rhyd)*np.sqrt(1+(19*a**2*deltaE)/(32*rhyd))
sigmak[i] = ordnung[i] - np.sqrt(4/a * np.sqrt(DeltaE/rhyd) - 5*DeltaE/rhyd)*np.sqrt(1+(19*a**2*DeltaE)/(32*rhyd))
np.savetxt('build/ekphik.txt', np.column_stack([ordnung, ordnung2, phik, thetak, ek, sigmak]), header='ordnung, ordnung2, phik, thetak, ek, sigmak')

def f(k, m, b):
    return m*k+b
params, covariance_matrix = optimize.curve_fit(f, ordnung2[:4], ek[:4])
errors = np.sqrt(np.diag(covariance_matrix))
m = ufloat(params[0], errors[0])
b = ufloat(params[1], errors[1])
print('Steigung:', m, params[0], errors[0])
print('Abschnitt:',b, params[1], errors[1])

x = np.linspace(850,1650,3)
print('Moseley')
plt.plot(ordnung2[:4], ek[:4], 'bx', label='Werte')
plt.plot(x, f(x, *params), 'k-', label='Ausgleichsgerade')
plt.xlabel(r'$\text{Z}^2$')
plt.ylabel(r'$E_\text{k}\;/\;\si{\electronvolt}$')
plt.xlim(850, 1650)
plt.ylim(9200, 19000)
plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig('build/moseley.pdf')
plt.clf()

print('Brom')
phibr, impbr = np.genfromtxt('python/brom.txt', unpack=True)
plt.plot(phibr, impbr, 'bx')
plt.xlabel(r'$φ\;/\;\si{\degree}$')
plt.ylabel('Counts')
plt.xlim(22.8, 29.2)
plt.ylim(15, 60)
plt.grid()
plt.tight_layout()
plt.savefig('build/brom.pdf')
plt.clf()

print('Strontium')
phistr, impstr = np.genfromtxt('python/strontium.txt', unpack=True)
plt.plot(phistr, impstr, 'gx')
plt.xlabel(r'$φ\;/\;\si{\degree}$')
plt.ylabel('Counts')
plt.xlim(18.8, 25.2)
plt.ylim(40, 200)
plt.grid()
plt.tight_layout()
plt.savefig('build/strontium.pdf')
plt.clf()

print('Zink')
phizn, impzn = np.genfromtxt('python/zink.txt', unpack=True)
plt.plot(phizn, impzn, 'rx')
plt.xlabel(r'$φ\;/\;\si{\degree}$')
plt.ylabel('Counts')
plt.xlim(32.8, 39.2)
plt.ylim(50, 110)
plt.grid()
plt.tight_layout()
plt.savefig('build/zink.pdf')
plt.clf()

print('Zirkonium')
phizr, impzr = np.genfromtxt('python/zirkonium.txt', unpack=True)
plt.plot(phizr, impzr, 'cx')
plt.xlabel(r'$φ\;/\;\si{\degree}$')
plt.ylabel('Counts')
plt.xlim(15.8, 24.2)
plt.ylim(110, 300)
plt.grid()
plt.tight_layout()
plt.savefig('build/zirkonium.pdf')
plt.clf()

print('Quecksilber')
phiqu, impqu = np.genfromtxt('python/quecksilber.txt', unpack=True)
plt.plot(phiqu, impqu, 'mx')
plt.xlabel(r'$φ\;/\;\si{\degree}$')
plt.ylabel('Counts')
plt.xlim(21.8, 31.2)
plt.ylim(25, 55)
plt.grid()
plt.tight_layout()
plt.savefig('build/quecksilber.pdf')
plt.clf()

m = len(phiqu)
phibr1 = np.zeros(m)
impbr1 = np.zeros(m)
phistr1 = np.zeros(m)
impstr1 = np.zeros(m)
phizn1 = np.zeros(m)
impzn1 = np.zeros(m)
for i in range(len(phibr)):
    phibr1[i] = phibr[i]
    impbr1[i] = impbr[i]
    phistr1[i] = phistr[i]
    impstr1[i] = impstr[i]
    phizn1[i] = phizn[i]
    impzn1[i] = impzn[i]
phizr1 = np.zeros(m)
impzr1 = np.zeros(m)
for i in range(len(phizr)):
    phizr1[i] = phizr[i]
    impzr1[i] = impzr[i]

np.savetxt('build/absorption.txt', np.column_stack([phibr1, impbr1, phistr1, impstr1, phizn1, impzn1, phizr1, impzr1, phiqu, impqu]), header='br str zn zr qu')
