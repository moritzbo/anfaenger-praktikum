import numpy as np
from uncertainties import ufloat
from scipy.stats import sem
import uncertainties.unumpy as unp

u, te = np.genfromtxt('python/daten/nachentladung.txt', unpack=True)
te = te*10**(-3)

temean = np.mean(te)
tesem = sem(te)
tem = ufloat(temean, tesem)
print('tem', tem)

te = te/u
temean = np.mean(te)
tesem = sem(te)
utem = ufloat(temean, tesem)
umean = np.mean(u)
usem = sem(u)
um = ufloat(umean, usem)
utem = utem * um
print('utem', utem)
np.savetxt('build/nachentladung.txt',
        np.column_stack([tem.n, tem.s, utem.n, utem.s]),
        header='tem, utem')
