import numpy as np
import matplotlib.pyplot as plt

v, ubr, us = np.genfromtxt('python/werte-e.txt', unpack=True)
w01 = 10**9 / (2 * np.pi * 993 * 332)
u = ubr / us
w = np.linspace(0, 2.5 * 10**4, 1000)
w0 = np.ones(1000)
w0 *= w01
o1 = w / w0
u1 = np.sqrt(1/9 * ((o1**2 - 1)**2)/((1 - o1**2)**2 + 9 * o1**2))
w0 = np.ones(len(v))
w0 *= w01
o = v / w0

plt.plot(o, u, 'rx', label='Messwerte')
plt.plot(o1, u1, 'b-', label='Theoriekurve')
plt.legend()
plt.grid()
plt.xscale('log')
plt.xlabel(r'$\frac{ν}{ν_0}$')
plt.ylabel(r'$ \frac{U_\text{br}}{U_\text{s}}$')
plt.xlim(3.5 * 10**(-2), 50)
plt.ylim(0, 0.35)
plt.tight_layout(pad=0)
plt.savefig('build/frequenz.pdf', bbox_inches='tight', pad_inches=0)
np.savetxt('build/frequenz.txt', np.column_stack([v, ubr, us, o, u]), header='v/Hz Ubr/V Us/V v:v0 Ubr:Us')
plt.clf()

o3 = np.linspace(0.7, 2, 1000)
u3 = np.sqrt(1/9 * ((o3**2 - 1)**2)/((1 - o3**2)**2 + 9 * o3**2))
plt.plot(o, u, 'rx', label='Messwerte')
plt.plot(o3, u3, 'b-', label='Theoriekurve')
plt.legend()
plt.grid()
plt.xscale('log')
plt.xlabel(r'$\frac{ν}{ν_0}$')
plt.ylabel(r'$\frac{U_\text{br}}{U_\text{s}}$')
plt.xlim(0.7, 1.3)
plt.ylim(0, 0.05)
plt.tight_layout(pad=0)
plt.savefig('build/frequenz-klein.pdf', bbox_inches='tight', pad_inches=0)
