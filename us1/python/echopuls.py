import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy import optimize
from scipy.stats import sem

h, P1, P2, t, h_schieb = np.genfromtxt('python/daten/daempfung.txt', unpack=True)

h *= 1e-3  # h in meter
t *= 1e-6  # t in sekunden
h_schieb *= 1e-3  # s in meter

len = len(h)
c = np.linspace(0,len-1,len)

for i in range(len):
    c[i] = 2*h[i]/t[i]
mc = np.mean(c)
sc = sem(c)
cu = ufloat(mc, sc)
print(mc, '+/-', sc)
print(cu)
np.savetxt('build/echopuls.txt',
        np.column_stack([h, t, c]),
        header='h, t, c')

def f(x, m, b):
    return x*m+b

params, covariance_matrix = optimize.curve_fit(f, t, 2*h)
errors = np.sqrt(np.diag(covariance_matrix))
m = ufloat(params[0], errors[0])
b = ufloat(params[1], errors[1])
print('m', m)
print('b', b)

x = np.linspace(0, 90, 2)
plt.plot(t*10**6, 2*h, 'kx', label='Messwerte')
plt.plot(x, f(x, *params)*10**(-6), 'r-', label='Ausgleichsgerade')
plt.xlim(0, 90)
plt.ylim(0, 0.250)
plt.xlabel(r'$t\;/\;\si{\micro\second}$')
plt.ylabel(r'$2\cdot h\;/\;\si{\centi\meter}$')
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig('build/echopuls.pdf')
