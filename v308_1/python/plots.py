import matplotlib.pyplot as plt
import numpy as np


def Bvektor(x, k, L, R, I):
    return(2*np.pi*10**(-3)*k*I*((x+L)/np.sqrt((x+L)**2+R**2) - x/np.sqrt(x**2+R**2)))


print('Lange Spule')
m = np.linspace(-22, 6)
plt.plot(-m, Bvektor(m, 300, 16, 2.05, 0.75), 'r--', label="Theorie, I = 0,75 A")
plt.plot(-m, Bvektor(m, 300, 16, 2.05, 1), 'k--', label="Theorie, I = 1 A")
xl, bl = np.genfromtxt('python/daten/lange-spule.txt', unpack=True)
plt.plot(xl, bl, 'o', label="Messwerte", markersize=3)
plt.xlabel(r'x / \si{\centi\metre}')
plt.ylabel(r'B / \si{\milli\tesla}')
plt.xlim(-6, 22)
plt.ylim(0, 3.7)
plt.tight_layout(pad=0)
plt.legend()
plt.grid()
plt.savefig('build/lange-spule.pdf', bbox_inches='tight', pad_inches=0)
plt.clf()

print('Kurze Spule')
xk, bk = np.genfromtxt('python/daten/kurze-spule.txt', unpack=True)
xk = xk - 4.5
m = np.linspace(-11, 5)
plt.plot(-m, Bvektor(m, 100, 5.5, 2.05, 2), 'r--', label="Theorie I, = 2 A")
plt.plot(-m, Bvektor(m, 100, 5.5, 2.05, 1), 'k--', label="Theorie I, = 1 A")
plt.plot(xk, bk, 'o', label='Messwerte', markersize=3)
plt.xlabel(r'x / \si{\centi\metre}')
plt.ylabel(r'B / \si{\milli\tesla}')
plt.xlim(-5, 11)
plt.ylim(-0.1, 2.2)
plt.tight_layout(pad=0)
plt.legend()
plt.grid()
plt.savefig('build/kurze-spule.pdf', bbox_inches='tight', pad_inches=0)
plt.clf()

print('Hysterese')
i, bh = np.genfromtxt('python/daten/hysterese.txt', unpack=True)
i1 = i[0:10]
i2 = i[10::]
bh1 = bh[0:10]
bh2 = bh[10::]

plt.plot(i1, bh1, 'rx', label='Neukurve', markersize=5)
plt.plot(i2, bh2, 'bo', label='Hysterse', markersize=3)
plt.xlabel(r'I / \si{\ampere}')
plt.ylabel(r'B / \si{\milli\tesla}')
plt.xlim(-10.5, 10.5)
plt.ylim(-750, 750)
plt.tight_layout(pad=0)
plt.grid()
plt.legend()
plt.savefig('build/hysterese.pdf', bbox_inches='tight', pad_inches=0)
plt.clf()

print('Helmholtz 7cm')
x, b = np.genfromtxt('python/daten/helmholtz-7.txt', unpack=True)
x1 = x[0:15]
x2 = x[15::]
b1 = b[0:15]
b2 = b[15::]
plt.subplot(1, 2, 1)
plt.plot(x1, b1, 'ro', label='Innen', markersize=3)
t = np.linspace(0.5, 2.3)
b7t = (4*np.pi*3*(6.25)**2)/((((6.25)**2)+((7/2)**2))**(3/2))
b7 = b7t*np.ones(len(t))
plt.plot(t, b7, 'k-', label="Theorie")
plt.xlabel(r'x / \si{\centi\metre}')
plt.ylabel(r'B / \si{\milli\tesla}')
plt.xlim(0.5, 2.3)
plt.grid()
plt.legend(loc='center')

plt.subplot(1, 2, 2)
plt.plot(x2, b2, 'bo', label='Außen', markersize=3)
plt.xlabel(r'x / \si{\centi\metre}')
plt.xlim(7, 16)
plt.ylim(0, 3.8)
plt.grid()
plt.legend()

plt.tight_layout(pad=0)
plt.savefig('build/helmholtz-7.pdf', bbox_inches='tight', pad_inches=0)
plt.clf()

print('Helmholtz 8cm')
x, b = np.genfromtxt('python/daten/helmholtz-8.txt', unpack=True)
x1 = x[0:25]
x2 = x[25::]
b1 = b[0:25]
b2 = b[25::]
plt.subplot(1, 2, 1)
plt.plot(x1, b1, 'ro', label='Innen', markersize=3)
t = np.linspace(0.5, 3.3)
b8t = (4*np.pi*3*(6.25)**2)/((((6.25)**2)+((8/2)**2))**(3/2))
b8 = b8t*np.ones(len(t))
plt.plot(t, b8, 'k-', label="Theorie")
plt.xlabel(r'x / \si{\centi\metre}')
plt.ylabel(r'B / \si{\milli\tesla}')
plt.xlim(0.5, 3.3)
plt.grid()
plt.legend(loc='center')

plt.subplot(1, 2, 2)
plt.plot(x2, b2, 'bo', label='Außen', markersize=3)
plt.xlabel(r'x / \si{\centi\metre}')
plt.xlim(8, 17)
plt.ylim(0, 3.4)
plt.grid()
plt.legend()

plt.tight_layout(pad=0)
plt.savefig('build/helmholtz-8.pdf', bbox_inches='tight', pad_inches=0)
plt.clf()

print('Helmholtz 9cm')
x, b = np.genfromtxt('python/daten/helmholtz-9.txt', unpack=True)
x1 = x[0:35]
x2 = x[35::]
b1 = b[0:35]
b2 = b[35::]
plt.subplot(1, 2, 1)
plt.plot(x1, b1, 'ro', label='Innen', markersize=3)
t = np.linspace(0.5, 4.3)
b9t = (4*np.pi*3*(6.25)**2)/((((6.25)**2)+((9/2)**2))**(3/2))
b9 = b9t*np.ones(len(t))
plt.plot(t, b9, 'k-', label="Theorie")
plt.xlabel(r'x / \si{\centi\metre}')
plt.ylabel(r'B / \si{\milli\tesla}')
plt.xlim(0.5, 4.3)
plt.grid()
plt.legend(loc='center')

plt.subplot(1, 2, 2)
plt.plot(x2, b2, 'bo', label='Außen', markersize=3)
plt.xlabel(r'x / \si{\centi\metre}')
plt.xlim(9, 19)
plt.ylim(0, 3.07)
plt.grid()
plt.legend()

plt.tight_layout(pad=0)
plt.savefig('build/helmholtz-9.pdf', bbox_inches='tight', pad_inches=0)
plt.clf()
