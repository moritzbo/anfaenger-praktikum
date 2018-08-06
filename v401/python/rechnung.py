import numpy as np
import uncertainties.unumpy as unumpy
from uncertainties import ufloat
from scipy.stats import sem

print('Wellenlaenge')
dd1, za = np.genfromtxt('python/wellenlaenge.txt', unpack=True)
dd = (dd1*10**(-3))/5.017
lam = 2 * dd / za
mlam = np.mean(lam)
slam = sem(lam)
rlam = ufloat(mlam, slam)
np.savetxt('build/wellenlaenge.txt', np.column_stack([dd1, dd, za, lam]), header='dd1, dd, za, lam')

print('Vakuum')
dp, zb = np.genfromtxt('python/vakuum.txt', unpack=True)
dn = zb * 650*10**(-9) / (2 * 0.05)
mdn = np.mean(dn)
sdn = sem(dn)
rdn = ufloat(mdn, sdn)
n = 1 + rdn * 295.15 * 1.0132 / (273.15*0.8)
print('rlam =',rlam)
print('rdn =',rdn)
print('n =',n)
np.savetxt('build/vakuum.txt', np.column_stack([dp, zb, dn]), header='dp, zb, delta n')
