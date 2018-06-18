import numpy as np
import matplotlib.pyplot as plt

print('Leistung ANFANG')
n, U, sU, I, sI = np.genfromtxt('python/daten/werte_c.txt', unpack=True)

i = I / 1000  # Skalierungsfaktor betrachten
u = U * 0.1
r = u / i
p = u * i
u0 = 1.4608
u01 = 1.5
ri = 5.64
ri1 = 6.2


def uk(i, u, r):
    return(u + i * r)


m = np.linspace(0.03, 0.11)
plt.plot(r, p, 'rx', label='Messwerte')
plt.plot(uk(m, u0, ri) / m, uk(m, u0, ri) * m, 'k-', label='Theoriekurve-1')
plt.plot(uk(m, u0, ri1) / m, uk(m, u0, ri1) * m, 'b-', label='Theoriekurve-2')
plt.plot(uk(m, u01, ri) / m, uk(m, u01, ri) * m, 'g-', label='Theoriekurve-3')
plt.legend()
plt.grid()
plt.xlim(20, 50)
plt.ylim(0.05, 0.2)
plt.xlabel(r'$R_\text{v} \:/\: \si{\ohm}$')
plt.ylabel(r'$P \:/\: \si{\milli\watt}$')
plt.tight_layout(pad=0)
plt.savefig('build/leistung.pdf', bbox_inches='tight', pad_inches=0)
np.savetxt('build/leistung.txt', np.column_stack([u, i, r, p]), header='U/V I/A R/ohm P/W')
plt.clf()
print('Leistung ENDE')
