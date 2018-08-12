import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy import optimize

h_mess, U1, U2, t, x_schieb = np.genfromtxt('python/daten/daempfung.txt', unpack=True)

def efunc(y, m, b):
    return np.e**(b+m*y)

params, covariance_matrix = optimize.curve_fit(efunc, x_schieb, U2)
errors = np.sqrt(np.diag(covariance_matrix))
m = ufloat(params[0], errors[0])
b = ufloat(params[1], errors[1])
print('m', m)
print('b', b)

x = np.linspace(20, 130)
plt.plot(x_schieb, U2, 'k.', label='Messwerte')
plt.plot(x, efunc(x, *params), 'r-', label='Fitfunktion')
plt.plot()
plt.grid()
plt.xlabel(r"$h\;/\;\si{\milli\meter}$")
plt.ylabel(r"$U\;/\;\si{\volt}$")
plt.legend()
plt.xlim(20, 130)
plt.ylim(0, 2)
plt.tight_layout()
plt.savefig('build/daempfefit.pdf')

plt.clf()

np.savetxt('build/daempfwerte.txt',
    np.column_stack([x_schieb, U2]),
    header='x_schieb, U2')
