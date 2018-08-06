import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 0, 51)
y = np.linspace(0, 1, 51)
t = np.ones(51)

# Rechteck
plt.xlabel('t')
plt.ylabel('Amplitude')
plt.xlim(-1, 1)
plt.ylim(-2.2, 2.2)

plt.plot(x, -2*t, 'g-', label=r'$\text{sign}(x)\symup{A}$')
plt.plot(y, 2*t, 'g-')

plt.xticks([-1, 0, 1], [r"$-\frac{\symup{T}}{2}$", 0, r"$\frac{\symup{T}}{2}$"])
plt.yticks([-2, 0, 2], [r"$-\symup{A}$", 0, r"$\symup{A}$"])
plt.legend()
plt.grid()
plt.savefig('build/recht.pdf')
plt.clf()

# Dreieck
plt.xlabel('t')
plt.ylabel('Amplitude')
plt.ylim(-2, 2)
plt.xlim(-1, 1)

plt.plot(x, -4*x-2, 'y-', label=r'$\frac{4\symup{A}}{\symup{T}}|t|-\symup{A}$')
plt.plot(y, 4*y-2, 'y-')

plt.xticks([-1, 0, 1], [r"$-\frac{\symup{T}}{2}$", 0, r"$\frac{\symup{T}}{2}$"])
plt.yticks([-2, 0, 2], [r"$-\symup{A}$", 0, r"$\symup{A}$"])
plt.legend()
plt.grid()
plt.savefig('build/dreieck.pdf')
plt.show()
plt.clf()

# Saegezahn
plt.xlabel('t')
plt.ylabel('Amplitude')
plt.xlim(-1, 1)
plt.ylim(-2, 2)

x = np.linspace(-1, 1, 101)
plt.plot(x, 2*x, 'b-', label=r'$\frac{2\symup{A}}{\symup{T}}t$')

plt.xticks([-1, 0, 1], [r"$-\frac{\symup{T}}{2}$", 0, r"$\frac{\symup{T}}{2}$"])
plt.yticks([-2, 0, 2], [r"$-\symup{A}$", 0, r"$\symup{A}$"])
plt.legend()
plt.grid()
plt.show()
plt.savefig('build/saege.pdf')
