import numpy as np
from uncertainties import ufloat
from scipy import optimize
import matplotlib.pyplot as plt

print("-------------doppelspalt1--------------")

doppel1, Int1 = np.genfromtxt('python/doppelspalt1.txt', unpack=True)
dsg2 = 0.875  # abstand schirm gitter in meter
g1 = 0.5e-3  # in meter
λ = 635e-9  # in meter
mdoppel1 = 0.0247
doppel1 = doppel1*10**(-3)
phi = np.arctan((doppel1-mdoppel1)/dsg2)
Int1 = Int1/6.5
phi1 = np.linspace(0.018,0.032,45)
phi2 = np.arctan((phi1-mdoppel1)/dsg2)
#z = 635e-9
def fitty(x1, s, b, z):
    return ((np.cos(np.pi*s*np.sin(x1)/z))**2*(z/(np.pi*b*np.sin(x1)))**2*(np.sin(np.pi*b*np.sin(x1)/z))**2)


# fit
params, covariance_matrix = optimize.curve_fit(fitty, phi, Int1, p0=[0.00005, 0.155e-3, 635e-9])
errors = np.sqrt(np.diag(covariance_matrix))
s = params[0]
b = params[1]
z = params[2]
plt.plot(doppel1, Int1, "k.", label='Messdaten')
plt.plot(phi1, fitty(phi2, *params), label="Fitfunktion")
print('s =', params[0], '+-', errors[0])
print('b =', params[1], '+-', errors[1])
print('z =', params[2], '+-', errors[2])

# print('l =', params[2], '+-', errors[2])

b = ufloat(params[0], errors[0])

plt.xlabel(r'$\symup{ds} \:/\: \si{\meter}$')
plt.ylabel(r'$\symup{I} \:/\: \si{\ampere}$')
plt.legend()
plt.grid()
plt.savefig('build/doppelspalt1_1.pdf', bbox_inches='tight',pad_inches =0)
plt.clf()

# ---------------------------
#s = 0.15e-3  # spaltabstand in meter
#sb = 0.5e-3  # spaltbreite in meter
#phi = np.arctan(doppel1/dsg2)
## B2 = np.cos((np.pi*s*np.sin(phi))/λ)**2*(λ/(np.pi*g1*np.sin(phi)))**2*(np.sin((np.pi*g1*np.sin(phi))/λ)**2)
#eta = (np.pi*sb*np.sin(phi))/λ
#B_neu = (sb*np.sin(eta))/(eta)
#
#
#def fitfunc3(z, f, k):
#
#    return (f*np.sin(k*z))/(k*z)
#
#
#params, covariance_matrix = optimize.curve_fit(fitfunc3, phi, B_neu)
#errors = np.sqrt(np.diag(covariance_matrix))
#print('f =', params[0], '+-', errors[0])
#print('k =', params[1], '+-', errors[1])
#
#f = ufloat(params[0], errors[0])
#
## plt.plot(phi, B_neu, "g.", label="Messdaten")
#plt.plot(phi, fitfunc3(phi, *params), label="Fitfunktion 4")
#plt.plot(doppel1, Int1, "k.", label="Messwerte")
#plt.xlabel(r'$\symup{ds} \:/\: \si{\meter}$')
#plt.ylabel(r'$\symup{I} \:/\: \si{\ampere}$')
#plt.legend()
#plt.grid()
#plt.savefig("build/doppelspalt1_2.pdf")
#plt.clf()
#
