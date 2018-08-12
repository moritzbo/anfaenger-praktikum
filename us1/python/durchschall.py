import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy import optimize
from scipy.stats import sem

t1, t2, s_schieb = np.genfromtxt('python/daten/durchschallung.txt', unpack=True)

t1 *= 1e-6  # t in sekunden
t2 *= 1e-6  # t in sekunden
s_schieb *= 1e-3  # s in meter
length = len(t1)

t = np.ones(length+2)
s = np.ones(length+2)
t[0] = t2[0]
t[1] = t2[1]
s[0] = s_schieb[0]
s[1] = s_schieb[1]
i = 2
while i < length+2:
    t[i] = t1[i-2]
    s[i] = s_schieb[i-2]
    i += 1
c = np.ones(length+2)
c[0] = 3*s_schieb[0]/t2[0]
c[1] = 3*s_schieb[1]/t2[1]
i = 2
while i < length+2:
    c[i] = s_schieb[i-2]/t1[i-2]
    i += 1
cm = np.mean(c)
dc = sem(c)
uc = ufloat(cm, dc)
print('c = ', cm, '+/-', dc)
print('c = ', uc)


np.savetxt('build/durchschall.txt',
        np.column_stack([s, t, c]),
        header='s, t, c')
def linreg(x, a, b):
    return a*x+b


params, covariance_matrix = optimize.curve_fit(linreg, t1, s_schieb)
errors = np.sqrt(np.diag(covariance_matrix))

a = ufloat(params[0], errors[0])
b = ufloat(params[1], errors[1])
print('Steigung m =', a)
print('Abschnitt b =', b)

x = np.linspace(0, 47)
plt.plot(t1*10**6, s_schieb*10**2, "kx", label="Messwerte")
plt.plot(x, linreg(x*10**(-4), *params), "r-", label="Ausgleichsgerade")
plt.xlabel(r"$t\;/\;\si{\micro\second}$")
plt.ylabel(r"$s\;/\;\si{\centi\meter}$")
plt.xlim(0, 47)
plt.ylim(0, 13)
plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig("build/durchschall.pdf")

plt.clf()
