import numpy as np
from uncertainties import ufloat
from scipy import optimize
import matplotlib.pyplot as plt

print("---------------einzelspalt---------------")
dx1, i1 = np.genfromtxt("python/einzelspalt.txt", unpack=True)
dsg = 0.325  # abstand schirm gitter in meter
g = 0.075e-3  # in meter
λ = 635e-9  # in meter
dx1 = dx1*10**(-3) # in Metern
mdx1 = 0.024 # Verschiebung Hauptmaxima in Meter
phi = np.arctan((dx1-mdx1)/dsg)
i1 = i1/0.78
phi1 = np.linspace(0.019,0.030)
phi2 = np.arctan((phi1-mdx1)/dsg)

def fitfunc2(phi, A, b):
    return (A**2*b**2*(np.sinc(b*np.sin(phi)/λ))**2)

params, covariance_matrix = optimize.curve_fit(fitfunc2, phi, i1, p0=[1000, 1e-3])
errors = np.sqrt(np.diag(covariance_matrix))
print('A =', params[0], '+-', errors[0])
print('b =', params[1], '+-', errors[1])

plt.plot(dx1, i1, "g.", label="Messdaten")
plt.plot(phi1, fitfunc2(phi2, *params), label="Fitfunktion")
plt.xlabel(r'$x\:/\:\si{\meter}$')
plt.ylabel(r'$I\:/\:\si{\ampere}$')
plt.legend()
plt.grid()
plt.xlim(0.019,0.030)
plt.ylim(0,1.1)
plt.savefig('build/einzelspalt1.pdf')
plt.clf()
