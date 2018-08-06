import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy import optimize
import uncertainties.unumpy as unp

distanz = np.linspace(0,8,3)

def fit(x, a, b):
    return a*x + b


D500, Ud500 = np.genfromtxt("python/D0.txt", unpack=True)
D500 *= 6e-3  # für länge in metern
params500, covariance_matrix500 = optimize.curve_fit(fit, Ud500, D500)
errors500 = np.sqrt(np.diag(covariance_matrix500))
Empf500 = ufloat(params500[0],errors500[0])
b500 = ufloat(params500[1],errors500[1])
print("Empfindlichkeit für 500:", Empf500)
print('b =', b500)


D450, Ud450, Ud400 = np.genfromtxt("python/D4_D5.txt", unpack=True)

D450 *= 6e-3  # für länge in metern
params450, covariance_matrix450 = optimize.curve_fit(fit, Ud450, D450)
errors450 = np.sqrt(np.diag(covariance_matrix450))
Empf450 = ufloat(params450[0],errors450[0])
b450 = ufloat(params450[1],errors450[1])
print("Empfindlichkeit für 450:", Empf450)
print('b =', b450)

params400, covariance_matrix400 = optimize.curve_fit(fit, Ud400, D450)
errors400 = np.sqrt(np.diag(covariance_matrix400))
Empf400 = ufloat(params400[0],errors400[0])
b400 = ufloat(params400[1],errors400[1])
print("Empfindlichkeit für 400:", Empf400)
print('b =', b400)

D350, Ud350, Ud300 = np.genfromtxt("python/D1_D2.txt", unpack=True)

D350 *= 6e-3  # für länge in metern
params350, covariance_matrix350 = optimize.curve_fit(fit, Ud350, D350)
errors350 = np.sqrt(np.diag(covariance_matrix350))
Empf350 = ufloat(params350[0],errors350[0])
b350 = ufloat(params350[1],errors350[1])
print("Empfindlichkeit für 350:", Empf350)
print('b =', b350)

params300, covariance_matrix300 = optimize.curve_fit(fit, Ud300, D350)
errors300 = np.sqrt(np.diag(covariance_matrix300))
Empf300 = ufloat(params300[0],errors300[0])
b300 = ufloat(params300[1],errors300[1])
print("Empfindlichkeit für 300:", Empf300)
print('b =', b300)

licens = np.linspace(-40,25,2)
plt.plot(Ud500, D500*10**3, 'bx', label=r'$\SI{500}{\volt}$', markersize=4)
plt.plot(Ud450, D450*10**3, 'gx', label=r'$\SI{450}{\volt}$', markersize=4)
plt.plot(Ud400, D450*10**3, 'rx', label=r'$\SI{400}{\volt}$', markersize=4)
plt.plot(Ud350, D350*10**3, 'yx', label=r'$\SI{350}{\volt}$', markersize=4)
plt.plot(Ud300, D350*10**3, 'kx', label=r'$\SI{300}{\volt}$', markersize=4)
plt.plot(licens, fit(licens, *params500)*10**3, 'b-', linewidth=1)
plt.plot(licens, fit(licens, *params450)*10**3, 'g-', linewidth=1)
plt.plot(licens, fit(licens, *params400)*10**3, 'r-', linewidth=1)
plt.plot(licens, fit(licens, *params350)*10**3, 'y-', linewidth=1)
plt.plot(licens, fit(licens, *params300)*10**3, 'k-', linewidth=1)
plt.xlabel(r'$U_d\;/\;\si{\volt}$')
plt.ylabel(r'$D\;/\;\si{\milli\meter}$')
plt.xlim(-40,25)
plt.ylim(-6,53)
plt.yticks(D350*10**3)
plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig('build/fitefeld.pdf')
plt.clf()

EMP = np.array([unp.nominal_values(Empf300),
                unp.nominal_values(Empf350),
                unp.nominal_values(Empf400),
                unp.nominal_values(Empf450),
                unp.nominal_values(Empf500)])

print("------------zweiter teil--------")

ub = np.array([300, 350, 400, 450, 500])  # beschleunigungsspannung in Volt
UB = 1 / ub
print("Array der Empfindlichkeit", EMP)
print("inverse Ub:", UB)
m = np.linspace(0.11,0.19)

def empfi(x, a6, b6):
    return a6*x + b6


params6, covariance_matrix = optimize.curve_fit(empfi, UB, EMP)
errors6 = np.sqrt(np.diag(covariance_matrix))
a6 = ufloat(params6[0], errors6[0])
b6 = ufloat(params6[1], errors6[1])
print('a6 =', a6)
print('b6 =', b6)
linsp = np.linspace(0.00175, 0.0035, 2)
plt.plot(UB*10**3, EMP*10**3, "kx", label="Empfindlichkeit")
plt.plot(linsp*10**3, empfi(linsp, *params6)*10**3, "r-", label="linearer fit")
plt.xlabel(r"$\sfrac{\num{e3}}{U_B}\;\;/\;\;\sfrac{1}{\si{\volt}}$")
plt.ylabel(r"$\text{Empfindlichkeit}\;/\;\si{\milli\meter\per\volt}$")
plt.xlim(1.75,3.5)
plt.ylim(0.5,1.2)
plt.legend()
plt.grid()
plt.savefig("build/empfindlichkeit.pdf")
plt.clf()

L = 0.143  # mittlerer weg zwischen y und schirm in meter
p = 0.019  # abstand der y platten in meter
d = 0.0038  # länge der y platte in meter
Ma = (p*L)/(2*d)
print("Materialgröße M", Ma)
