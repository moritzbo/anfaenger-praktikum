import numpy as np
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import sem

print('====================')
print('Widerstand ANFANG')
print('====================')
print('Wert 12 ANFANG')
ra2 = ufloat(1000, 1000 * 0.002)
pot1a = 2.82
pot1b = 10 - pot1a
pot1c = pot1a / pot1b
pota = ufloat(pot1c, pot1c * 0.005)
ra1 = ra2 * pota
print('ra1', ra1)

rb2 = ufloat(664, 664 * 0.002)
pot2a = 3.73
pot2b = 10 - pot2a
pot2c = pot2a / pot2b
potb = ufloat(pot2c, pot2c * 0.005)
rb1 = rb2 * potb
print('rb1', rb1)

rc2 = ufloat(332, 332 * 0.002)
pot3a = 5.42
pot3b = 10 - pot3a
pot3c = pot3a / pot3b
potc = ufloat(pot3c, pot3c * 0.005)
rc1 = rc2 * potc
print('rc1', rc1)

r = np.array([unp.nominal_values(ra1), unp.nominal_values(rb1), unp.nominal_values(rc1)])
d = np.array([unp.std_devs(ra1), unp.std_devs(rb1), unp.std_devs(rc1)])
np.savetxt('build/wert12.txt', np.column_stack([r, d]), header='r d')
print('r-mean', r.mean())
print('r-std', sem(r))
print('Wert 12 ENDE')

print('====================')

print('Wert 13 ANFANG')
ra2 = ufloat(1000, 1000 * 0.002)
pot1a = 2.44
pot1b = 10 - pot1a
pot1c = pot1a / pot1b
pota = ufloat(pot1c, pot1c * 0.005)
ra1 = ra2 * pota
print('ra1', ra1)

rb2 = ufloat(664, 664 * 0.002)
pot2a = 3.28
pot2b = 10 - pot2a
pot2c = pot2a / pot2b
potb = ufloat(pot2c, pot2c * 0.005)
rb1 = rb2 * potb
print('rb1', rb1)

rc2 = ufloat(332, 332 * 0.002)
pot3a = 4.91
pot3b = 10 - pot3a
pot3c = pot3a / pot3b
potc = ufloat(pot3c, pot3c * 0.005)
rc1 = rc2 * potc
print('rc1', rc1)

r = np.array([unp.nominal_values(ra1), unp.nominal_values(rb1), unp.nominal_values(rc1)])
d = np.array([unp.std_devs(ra1), unp.std_devs(rb1), unp.std_devs(rc1)])
np.savetxt('build/wert13.txt', np.column_stack([r, d]), header='r d')
print('r-mean', r.mean())
print('r-std', sem(r))
print('Wert 13 ENDE')
print('====================')
print('Widerstand ENDE')

print('===================')
