import numpy as np
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import sem

print('====================')
print('Kondensator ANFANG')
print('====================')
print('Wert 1 ANFANG')
cao2 = 994 * 10**(-9)
pot1 = 6.03
c2 = ufloat(cao2, cao2 * 0.002)
pot2 = 10 - pot1
pot3 = pot1 / pot2
pot = ufloat(pot3, pot3 * 0.005)
ca1 = c2 / pot
print('ca1', ca1)

cao2 = 750 * 10**(-9)
pot1 = 5.305
c2 = ufloat(cao2, cao2 * 0.002)
pot2 = 10 - pot1
pot3 = pot1 / pot2
pot = ufloat(pot3, pot3 * 0.005)
cb1 = c2 / pot
print('cb1', cb1)

cao2 = 399 * 10**(-9)
pot1 = 3.78
c2 = ufloat(cao2, cao2 * 0.002)
pot2 = 10 - pot1
pot3 = pot1 / pot2
pot = ufloat(pot3, pot3 * 0.005)
cc1 = c2 / pot
print('cc1', cc1)

c = np.array([unp.nominal_values(ca1), unp.nominal_values(cb1), unp.nominal_values(cc1)])
d = np.array([unp.std_devs(ca1), unp.std_devs(cb1), unp.std_devs(cc1)])
np.savetxt('build/wert1.txt', np.column_stack([c, d]), header='c d')
print('c-mean', c.mean())
print('c-std', sem(c))
print('Wert 1 ENDE')

print('====================')

print('Wert 3 ANFANG')
cao2 = 994 * 10**(-9)
pot1 = 7.05
c2 = ufloat(cao2, cao2 * 0.002)
pot2 = 10 - pot1
pot3 = pot1 / pot2
pot = ufloat(pot3, pot3 * 0.005)
ca1 = c2 / pot
print('ca1', ca1)

cao2 = 750 * 10**(-9)
pot1 = 6.395
c2 = ufloat(cao2, cao2 * 0.002)
pot2 = 10 - pot1
pot3 = pot1 / pot2
pot = ufloat(pot3, pot3 * 0.005)
cb1 = c2 / pot
print('cb1', cb1)

cao2 = 399 * 10**(-9)
pot1 = 4.89
c2 = ufloat(cao2, cao2 * 0.002)
pot2 = 10 - pot1
pot3 = pot1 / pot2
pot = ufloat(pot3, pot3 * 0.005)
cc1 = c2 / pot
print('cc1', cc1)

c = np.array([unp.nominal_values(ca1), unp.nominal_values(cb1), unp.nominal_values(cc1)])
d = np.array([unp.std_devs(ca1), unp.std_devs(cb1), unp.std_devs(cc1)])
np.savetxt('build/wert3.txt', np.column_stack([c, d]), header='c d')
print('c-mean', c.mean())
print('c-std', sem(c))
print('Wert 3 ENDE')

print('====================')

print('Wert 8 ANFANG')

cao2 = 994 * 10**(-9)
pot1 = 1.175
rao2 = 5000
c2 = ufloat(cao2, cao2 * 0.002)
pot2 = 10 - pot1
pot3 = pot1 / pot2
pot = ufloat(pot3, pot3 * 0.005)
ca1 = c2 / pot
r2 = ufloat(rao2, rao2 * 0.03)
ra1 = r2 * pot
print('ra1', ra1)
print('ca1', ca1)
print('.')

cao2 = 750 * 10**(-9)
pot1 = 4.35
rao2 = 875
c2 = ufloat(cao2, cao2 * 0.002)
pot2 = 10 - pot1
pot3 = pot1 / pot2
pot = ufloat(pot3, pot3 * 0.005)
cb1 = c2 / pot
r2 = ufloat(rao2, rao2 * 0.03)
rb1 = r2 * pot
print('rb1', rb1)
print('cb1', cb1)
print('.')

cao2 = 399 * 10**(-9)
pot1 = 5.78
rao2 = 410
c2 = ufloat(cao2, cao2 * 0.002)
pot2 = 10 - pot1
pot3 = pot1 / pot2
pot = ufloat(pot3, pot3 * 0.005)
cc1 = c2 / pot
r2 = ufloat(rao2, rao2 * 0.03)
rc1 = r2 * pot
print('rc1', rc1)
print('cc1', cc1)
print('.')

c = np.array([unp.nominal_values(ca1), unp.nominal_values(cb1), unp.nominal_values(cc1)])
dc = np.array([unp.std_devs(ca1), unp.std_devs(cb1), unp.std_devs(cc1)])
r = np.array([unp.nominal_values(ra1), unp.nominal_values(rb1), unp.nominal_values(rc1)])
dr = np.array([unp.std_devs(ra1), unp.std_devs(rb1), unp.std_devs(rc1)])
np.savetxt('build/wert8.txt', np.column_stack([c, dc, r, dr]), header='c stdc r stdr')
c = c[1::]
r = r[1::]
print('c-mean', c.mean())
print('c-std', sem(c))
print('r-mean', r.mean())
print('r-std', sem(r))

print('Wert 8 ENDE')
print('====================')
print('Kondensator ENDE')

print('====================')
