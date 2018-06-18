import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
from uncertainties import ufloat

n, ur, sUr, ir, sIr, us, sUs, iS, sIs = np.genfromtxt('python/daten/werte_d.txt', unpack=True)
print('Rechteck ANFANG')
ir1 = ir[0:9] / 10000  # Skalierungsfaktor betrachten
ir2 = ir[9::] / 10000
ur1 = ur[0:9] / 100
ur2 = ur[9::] / 100


def f(x, a, b):
    return a*x+b


params1, covariance_matrix1 = optimize.curve_fit(f, ir1, ur1)  # Fit Werte 1
errors1 = np.sqrt(np.diag(covariance_matrix1))
a1 = params1[0]
b1 = params1[1]
print('a1, b1', ufloat(params1[0], errors1[0]), ufloat(params1[1], errors1[1]))

params2, covariance_matrix2 = optimize.curve_fit(f, ir2, ur2)  # Fit Werte 2
errors2 = np.sqrt(np.diag(covariance_matrix2))
a2 = params2[0]
b2 = params2[1]
print('a2, b2', ufloat(params2[0], errors2[0]), ufloat(params2[1], errors2[1]))

m = np.linspace(0.002, 0.007)
plt.plot(ir1, ur1, 'rx', label='Messwerte-1')
plt.plot(ir2, ur2, 'gx', label='Messwerte-2')
plt.plot(m, a1*m + b1, 'k-', label='Ausgleichsgerade-1')
plt.plot(m, a2*m + b2, 'b-', label='Ausgleichsgerade-2')
plt.legend()
plt.grid()
plt.xlim(0.002, 0.007)
plt.ylim(0.3, 0.6)
plt.xlabel(r'$\symbf{I} \:/\: \si{\ampere}$')
plt.ylabel(r'$U_\text{k} \:/\: \si{\volt}$')
plt.tight_layout(pad=0)
plt.savefig('build/rechteck.pdf', bbox_inches='tight', pad_inches=0)
np.savetxt('build/rechteck1.txt', np.column_stack([ir1, ur1]), header='I/A U/V')
np.savetxt('build/rechteck2.txt', np.column_stack([ir2, ur2]), header='I/A U/V')
plt.clf()
print('Rechteck ENDE')

print('Sinus ANFANG')
is1 = iS[0:13] / 100000  # Skalierungsfaktor betrachten
is2 = iS[13::] / 100000
us1 = us[0:13] / 100
us2 = us[13::] / 100


def f(x, a, b):
    return a*x+b


params1, covariance_matrix1 = optimize.curve_fit(f, is1, us1)  # Fit Werte 1
errors1 = np.sqrt(np.diag(covariance_matrix1))
a1 = params1[0]
b1 = params1[1]
print('a1, b1', ufloat(params1[0], errors1[0]), ufloat(params1[1], errors1[1]))

params2, covariance_matrix2 = optimize.curve_fit(f, is2, us2)  # Fit Werte 2
errors2 = np.sqrt(np.diag(covariance_matrix2))
a2 = params2[0]
b2 = params2[1]
print('a2, b2', ufloat(params2[0], errors2[0]), ufloat(params2[1], errors2[1]))

m = np.linspace(0.0001, 0.0007)
plt.plot(is1, us1, 'rx', label='Messwerte-1')
plt.plot(is2, us2, 'gx', label='Messwerte-2')
plt.plot(m, a1*m + b1, 'k-', label='Ausgleichsgerade-1')
plt.plot(m, a2*m + b2, 'b-', label='Ausgleichsgerade-2')
plt.legend()
plt.grid()
plt.xlim(0.0001, 0.0007)
plt.ylim(0.6, 1)
plt.xlabel(r'$\symbf{I} \:/\: \si{\ampere}$')
plt.ylabel(r'$U_\text{k} \:/\: \si{\volt}$')
plt.tight_layout(pad=0)
plt.savefig('build/sinus.pdf', bbox_inches='tight', pad_inches=0)
np.savetxt('build/sinus1.txt', np.column_stack([is1, us1]), header='I/A U/V')
np.savetxt('build/sinus2.txt', np.column_stack([is2, us2]), header='I/A U/V')
plt.clf()
print('Sinus ENDE')
