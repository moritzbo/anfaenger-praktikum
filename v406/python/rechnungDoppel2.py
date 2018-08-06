import numpy as np
from uncertainties import ufloat
from scipy import optimize
import matplotlib.pyplot as plt


print("--------------------doppelspalt2------------------")

doppel2, Int2 = np.genfromtxt('python/doppelspalt2.txt', unpack=True)
dsg3 = 0.875  # abstand schirm gitter in meter
g3 = 0.075e-3  # in meter
λ = 635e-9  # in meter
doppel2 = doppel2*10**(-3)  # in Metern
mdoppel2 = 0.025  # Verschiebung Hauptmaxima in Meter
phi = np.arctan((doppel2-mdoppel2)/dsg3)
Int2 = Int2/3.9

print("erste methode")


def fitty(x1, s, b):
    return ((np.cos(np.pi*s*np.sin(phi)))**2*(λ/(np.pi*b*np.sin(phi)))**2*(np.sin(np.pi*b*np.sin(phi)/λ))**2)


# fit
params, covariance_matrix = optimize.curve_fit(fitty, phi, doppel2, p0=[1e-3, 0.115e-3])
errors = np.sqrt(np.diag(covariance_matrix))
print('s =', params[0], '+-', errors[0])
print('b =', params[1], '+-', errors[1])

#b = ufloat(params[0], errors[0])


plt.plot(doppel2, Int2, "g.", label="Messdaten")
plt.plot(doppel2, fitty(phi, *params), label="Fitfunktion")

# plt.plot(phi, ((np.cos(np.pi*0.075e-3*np.sin(phi)))**2*(λ/(np.pi*0.075e-3*np.sin(phi)))**2*(np.sin(np.pi*0.075e-3*np.sin(phi)/λ))**2))

plt.xlabel(r'$x \:/\: \si{\meter}$')
plt.ylabel(r'$I \:/\: \si{\ampere}$')
plt.legend()
plt.grid()
plt.savefig('build/doppelspalt2_1.pdf')
plt.clf()
