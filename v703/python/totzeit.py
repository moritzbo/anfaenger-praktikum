import numpy as np
from uncertainties import ufloat
from scipy.stats import sem
import uncertainties.unumpy as unp

u, tt = np.genfromtxt('python/daten/totzeit.txt', unpack=True)
tt = tt*10**(-6)

ttmean = np.mean(tt)
ttsem = sem(tt)
ttm = ufloat(ttmean, ttsem)
print('ttm', ttm)

tt = tt/u
ttmean = np.mean(tt)
ttsem = sem(tt)
uttm = ufloat(ttmean, ttsem)
print('uttm', uttm)

u, nn1, nn12, nn2 = np.genfromtxt('python/daten/zwei-quellen.txt', unpack=True)

nn1f = np.sqrt(nn1)/60
nn12f = np.sqrt(nn12)/60
nn2f = np.sqrt(nn2)/60

nn1 = nn1/60
nn12 = nn12/60
nn2 = nn2/60

n1 = ufloat(nn1, nn1f)
n12 = ufloat(nn12, nn12f)
n2 = ufloat(nn2, nn2f)

print('n1', n1)
print('n12', n12)
print('n2', n2)

T = (n1+n2-n12)/(2*n1*n2)
print('T', T)

np.savetxt('build/totzeit.txt',
np.column_stack([ttm.n, ttm.s, uttm.n, uttm.s, T.n, T.s]),
header='ttm, uttm, T')
