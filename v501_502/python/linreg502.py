import numpy as np
from uncertainties import ufloat
from scipy import optimize
import matplotlib.pyplot as plt
from scipy.stats import sem
import uncertainties.unumpy as unp
D1, I1, I2 = np.genfromtxt("python/502werte.txt", unpack=True)

# B Feld berechnen
reversed_I1 = np.fliplr([I1])[0]
reversed_I2 = np.fliplr([I2])[0]

D1 *= 6e-3  # wir müssen das auch in metern nehmen
L = 0.143  # wirkungsweite des B felds
Ub = np.array([250, 350])
r = 0.282  # in metern
N = 20  # Windungen
μ0 = 4*np.pi*10**(-7)
B1 = μ0*(8/np.sqrt(125))*((N*I1)/r) # in Tesla
B2 = μ0*(8/np.sqrt(125))*((N*I2)/r)
F = D1/(L**2 + D1**2)
np.savetxt('build/502.txt', np.column_stack([F, B1, B2]), header='F B1 B2')

def fitfunction(x, a, b):
    return a * x + b


params1, covariance_matrix = optimize.curve_fit(fitfunction, B1, F)
errors1 = np.sqrt(np.diag(covariance_matrix))
a1 = ufloat(params1[0], errors1[0])
b1 = ufloat(params1[1], errors1[1])
print('a1', a1)
print('b1',b1)

params2, covariance_matrix = optimize.curve_fit(fitfunction, B2, F)
errors2 = np.sqrt(np.diag(covariance_matrix))
a2 = ufloat(params2[0], errors2[0])
b2 = ufloat(params2[1], errors2[1])
print('a2', a2)
print('b2',b2)

linspac = np.linspace(0,200,2)
plt.plot(B1*10**6, F, "k.", label="Werte für Ub = 250V")
plt.plot(B2*10**6, F, "r.", label="Werte für Ub = 350V")
plt.plot(linspac, fitfunction(linspac, *params1)*10**(-6), "k-", label="Fit für Ub = 250V")
plt.plot(linspac, fitfunction(linspac, *params2)*10**(-6), "r-", label="Fit für Ub = 350V")
plt.xlabel(r"$B\;/\;\si{\micro\tesla}$")
plt.ylabel(r"$\frac{D}{(L^2+D^{\,2})}\;/\;\si{\per\meter}$")
plt.xlim(0, 200)
plt.ylim(0, 3)
plt.legend()
plt.grid()
plt.savefig("build/b_feld1.pdf")
plt.clf()

print("-------e0m0 bestimmung--------")
e0mo250 = (a1**2)*(8*Ub[0])
e0mo350 = (a2**2)*(8*Ub[1])
e0m0 = np.array([unp.nominal_values(e0mo250), unp.nominal_values(e0mo350)])
print('mean',ufloat(np.mean(e0m0),sem(e0m0)))
print("e0/m0250 =", e0mo250*1e-11, "in 10*11 C/kg")
print("e0/m0350 =", e0mo350*1e-11, "in 10*11 C/kg")

value = np.array([F, I1, B1, I2, B2])
np.savetxt("python/value.txt", np.column_stack([F, I1, B1, I2, B2]), header="F I1 B1 I2 B2")

print("-----------------502_b)-------------------")
phi = 80*np.pi/180  # rad
phi1 = 78*np.pi/180  # rad
Itot = 0.162 # ampere
Ub_tot = 180  # volt
Btot = μ0*(8/np.sqrt(125))*((N*Itot)/r)
Bhor = (Btot)/(np.cos(phi))
Bhor1 = (Btot)/(np.cos(phi1))
print("horizontalkomponente von B:", Bhor)
print("horizontalkomponente von B1:", Bhor1)
