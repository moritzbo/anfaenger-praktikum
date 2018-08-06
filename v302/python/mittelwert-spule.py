import numpy as np
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import sem

print('====================')
print('Spule Wert 17 ANFANG')
print('====================')
print('Induktivitätsmessbrücke ANFANG')
rao2 = 980
lao2 = 27.5 * 10**(-3)
pot1 = 0.865
r2 = ufloat(rao2, rao2 * 0.03)
l2 = ufloat(lao2, lao2 * 0.03)
pot2 = 10 - pot1
pot3 = pot1 / pot2
pot = ufloat(pot3, pot3 * 0.005)
ra1 = r2 * pot
la1 = l2 * pot
print('ra1', ra1)
print('la1', la1)
print('.')

rao2 = 2034
lao2 = 20.1 * 10**(-3)
pot1 = 0.5
r2 = ufloat(rao2, rao2 * 0.03)
l2 = ufloat(lao2, lao2 * 0.03)
pot2 = 10 - pot1
pot3 = pot1 / pot2
pot = ufloat(pot3, pot3 * 0.005)
rb1 = r2 * pot
lb1 = l2 * pot
print('rb1', rb1)
print('lb1', lb1)
print('.')

rao2 = 810
lao2 = 14.6 * 10**(-3)
pot1 = 1.1
r2 = ufloat(rao2, rao2 * 0.03)
l2 = ufloat(lao2, lao2 * 0.03)
pot2 = 10 - pot1
pot3 = pot1 / pot2
pot = ufloat(pot3, pot3 * 0.005)
rc1 = r2 * pot
lc1 = l2 * pot
print('rc1', rc1)
print('lc1', lc1)
print('.')

l = np.array([unp.nominal_values(la1), unp.nominal_values(lb1), unp.nominal_values(lc1)])
dl = np.array([unp.std_devs(la1), unp.std_devs(lb1), unp.std_devs(lc1)])
r = np.array([unp.nominal_values(ra1), unp.nominal_values(rb1), unp.nominal_values(rc1)])
dr = np.array([unp.std_devs(ra1), unp.std_devs(rb1), unp.std_devs(rc1)])
np.savetxt('build/wert17a.txt', np.column_stack([l, dl, r, dr]), header='l stdl r stdr')
print('l-mean', l.mean())
print('l-std', sem(l))
print('r-mean', r.mean())
print('r-std', sem(r))
print('Induktivitätsmessbrücke ENDE')

print('====================')

print('Maxwellbrücke ANFANG')
cao4 = 750 * 10**(-9)
rao2 = 1000
rao3 = 89
rao4 = 545
c4 = ufloat(cao4, cao4 * 0.002)
r2 = ufloat(rao2, rao2 * 0.002)
r3 = ufloat(rao3, rao3 * 0.03)
r4 = ufloat(rao4, rao4 * 0.03)
ra1 = r2 * r3 / r4
la1 = r2 * r3 * c4
print('ra1', ra1)
print('la1', la1)
print('.')

cao4 = 994 * 10**(-9)
rao2 = 1000
rao3 = 80.5
c4 = ufloat(cao4, cao4 * 0.002)
r2 = ufloat(rao2, rao2 * 0.002)
r3 = ufloat(rao3, rao3 * 0.03)
rb1 = r2 * r3
lb1 = r2 * r3 * c4
print('rb1max', rb1)
print('lb1', lb1)
print('.')

cao4 = 597 * 10**(-9)
rao2 = 1000
rao3 = 95
c4 = ufloat(cao4, cao4 * 0.002)
r2 = ufloat(rao2, rao2 * 0.002)
r3 = ufloat(rao3, rao3 * 0.03)
rc1 = r2 * r3
lc1 = r2 * r3 * c4
print('rc1max', rc1)
print('lc1', lc1)
print('.')

l = np.array([unp.nominal_values(la1), unp.nominal_values(lb1), unp.nominal_values(lc1)])
dl = np.array([unp.std_devs(la1), unp.std_devs(lb1), unp.std_devs(lc1)])
r = np.array([unp.nominal_values(ra1), unp.nominal_values(rb1), unp.nominal_values(rc1)])
dr = np.array([unp.std_devs(ra1), unp.std_devs(rb1), unp.std_devs(rc1)])
np.savetxt('build/wert17b.txt', np.column_stack([l, dl, r, dr]), header='l stdl r stdr')
print('l-mean', l.mean())
print('l-std', sem(l))
print('r-mean', r.mean())
print('r-std', r.std())

print('Maxwellbrücke ENDE')
print('====================')
print('Spule Wert 17 ENDE')

print('====================')
