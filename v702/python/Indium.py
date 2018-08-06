import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy import optimize
import scipy.constants as const
import uncertainties.unumpy as unp

N = np.genfromtxt("python/indium.txt", unpack=True)
fehler = 152
lenN = len(N)
t = np.linspace(1, lenN, lenN)
t = t *240
N = N - fehler
fehlerN = np.sqrt(N)
Nlog = np.log(N)
fehlerNlog = (fehlerN)/N

def fit(x, a, b):
    return -a*x + b

params, covariance_matrix = optimize.curve_fit(fit, t, Nlog)
errors = np.sqrt(np.diag(covariance_matrix))

a = ufloat(params[0], errors[0])
b = ufloat(params[1], errors[1])
print('a', a)
print('b', b)

Th_Ind = np.log(2)/a
print("Halbwertszeit von Indium:", Th_Ind, 's')
Th_Ind /= 60
print("Halbwertszeit von Indium:", Th_Ind, 'min')
lit = 54.28
prfe = 100*abs(lit-unp.nominal_values(Th_Ind))/lit
print('proz fehler', prfe)

x = np.linspace(0, 4000, 2)
plt.errorbar(t, Nlog, xerr=None, yerr=fehlerNlog, fmt='kx', markersize=5, label='Messwerte mit Fehler')
plt.plot(x, fit(x, *params), "r--", label="linearer Fit")
plt.grid()
plt.xlim(0, 4000)
plt.ylim(7.3, 8.2)
plt.xlabel(r"$t\;/\;\si{\second}$")
plt.ylabel(r"$\log(N)$")
plt.legend()
plt.savefig("build/Indiumfit.pdf")

plt.clf()

treal = np.linspace(0, 3700)
ft = np.exp(params[1]-params[0]*treal)
plt.errorbar(t, N, xerr=None, yerr=fehlerN, fmt="kx", label="Messwerte")
plt.plot(treal, ft, "r--", label="Exponential der Messwerte")
plt.grid()
plt.xlim(0, 3700)
plt.ylim(1550, 3400)
plt.xlabel(r"$t\;/\;\si{\second}$")
plt.ylabel(r"$N\;/\;\text{Anzahl}$")
plt.legend()
plt.savefig("build/Indiumwerte.pdf")

plt.clf()

np.savetxt('build/indium.txt',
        np.column_stack([t, N, fehlerN, Nlog, fehlerNlog]),
        header='t, N, fehlerN, Nlog, fehlerNlog')
