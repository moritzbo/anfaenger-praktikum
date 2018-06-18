import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
from uncertainties import ufloat

print('Monozelle ANFANG')
n, U, sU, I, sI = np.genfromtxt('python/daten/werte_b.txt', unpack=True)

# besonders betrachten und teilen
i1 = I[0:8] / 1000  # Skalierungsfaktor betrachten
i2 = I[8::] / 1000
i3 = I / 1000
u1 = U[0:8] * 0.1
u2 = U[8::] * 0.1
u3 = U * 0.1


def f(x, a, b):
    return a*x+b


params, covariance_matrix = optimize.curve_fit(f, i3, u3)  # Fit Werte
errors = np.sqrt(np.diag(covariance_matrix))
a = params[0]
b = params[1]
print('a, b', ufloat(params[0], errors[0]), ufloat(params[1], errors[1]))

m = np.linspace(0, 0.1)
plt.plot(i1, u1, 'rx', label='Skalierung-1')
plt.plot(i2, u2, 'gx', label='Skalierung-2')
plt.plot(m, a*m + b, 'b-', label='Ausgleichsgerade')
plt.legend()
plt.grid()
plt.xlim(0, 0.1)
plt.ylim(0.8, 1.5)
plt.xlabel(r'$\symbf{I} \:/\: \si{\ampere}$')
plt.ylabel(r'$U_\text{k} \:/\: \si{\volt}$')
plt.tight_layout(pad=0)
plt.savefig('build/mono.pdf', bbox_inches='tight', pad_inches=0)
np.savetxt('build/mono1.txt', np.column_stack([i1, u1]), header='I/A U/V')
np.savetxt('build/mono2.txt', np.column_stack([i2, u2]), header='I/A U/V')
plt.clf()
print('Monozelle ENDE')
