import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy import optimize
import scipy.constants as const

u, imp, i = np.genfromtxt('python/daten/impulse.txt', unpack=True) # V 1/s μs
anzmess = len(u)
impf = np.zeros(anzmess)

for k in range(anzmess):
    impf[k] = np.sqrt(imp[k])
    # Plateau von 390 - 610
    if u[k] == 390:
        panf = k
    if u[k] == 610:
        pend = k
    if u[k] == 490:
        p100 = k

impa = imp
imp = imp/60
impf = impf/60

q = const.elementary_charge
Q = np.zeros(anzmess)
dQ = np.zeros(anzmess)
for k in range(anzmess-1):
    Q[k+1] = (i[k+1]*10**(-6))/(imp[k+1]*q)
    dQ[k+1] = (impf[k+1]*i[k+1]*10**(-6))/(imp[k+1]**2*q)

def lin(x, m, b):
    return m*x+b

a = ufloat(imp[panf], impf[panf])
b = ufloat(imp[p100], impf[p100])
print('390, 490')
print('a', a, 'b', b,)
d = (b-a)/(b)*100
print('1', d)
a = 210
b = 212
d = (b-a)/(b)*100
print(d)
df = 2*100/b*np.sqrt((1-d)**2+1/b**2)
print(df)

params, covariance_matrix = optimize.curve_fit(lin, u[panf:pend+1], imp[panf:pend+1])
errors = np.sqrt(np.diag(covariance_matrix))
m = ufloat(params[0], errors[0])
b = ufloat(params[1], errors[1])
print('m', m)
print('b', b)
print('Plateau-Grenzen:', u[panf], u[pend])

xlimit = np.array([300, 710])
ylimit = np.array([185, 230])
plt.errorbar(u[1::], imp[1::], xerr=None, yerr=impf[1::], fmt='bx', markersize=5, label='Messwerte mit Fehler')
plt.plot(xlimit, lin(xlimit, *params), 'r-', label='Linearer Fit', markersize=3)
plt.plot([390, 390], [ylimit[0], 208], 'k-.', markersize=0.1, label='Plateau-Grenzen')
plt.plot([610, 610], [ylimit[0], 213], 'k-.', markersize=0.1)
plt.xlim(*xlimit)
plt.ylim(*ylimit)
plt.xlabel(r'$U\;/\;\si{\volt}$')
plt.ylabel(r'$N\;/\;\sfrac{1}{\,\SI{1}{\second}}$')
plt.grid()
plt.legend(loc='lower center')
plt.tight_layout()
plt.savefig('build/impulse.pdf')
plt.clf()

np.savetxt('build/impulse.txt',
        np.column_stack([u, impa, imp, impf, i, Q, dQ]),
        header='U/V, Imp/60s, Imp/1s, Impf, i/μA, Q/e, dQ/e')

plt.plot(u, Q*10**(-9), 'bx')
plt.xlim(290, 710)
plt.ylim(0, 0.6)
plt.xlabel(r'$U\;/\;\si{\volt}$')
plt.ylabel(r'$\increment Q\;/\;\num{e9}\symup{e}_0$')
plt.grid()
plt.tight_layout()
plt.savefig('build/ladung.pdf')
plt.clf()
