import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import sem
from uncertainties import ufloat
import uncertainties.unumpy as unp

# edv ist das kleinere

amp, t = np.genfromtxt('python/daten/herzwelle.txt', unpack=True)
amp *=10**(-3)
tiefe = 44.46*10**(-3)
durch = 49.4*10**(-3)
radius = durch/2
area = np.pi*radius**2
damp = tiefe - amp

anzmess = len(t)
f = np.ones(anzmess)
ed = np.ones(anzmess)
hzv = np.ones(anzmess)
fhzv = np.ones(anzmess)

for i in range(anzmess-1):
    f[i] = 1/(2*(t[i+1]-t[i]))

fn = f[0:-1]
mf = ufloat(np.mean(fn), sem(fn))
print('Mittelwert Frequenz', mf)

for i in range(anzmess):
    ed[i] = area * amp[i]

for i in range(1,anzmess):
    hzv[i] = abs(ed[i]-ed[i-1])*unp.nominal_values(mf)
    fhzv[i] = abs(ed[i]-ed[i-1])*unp.std_devs(mf)

hzvn = hzv[1::]
print('Mittelwert hzvn', np.mean(hzvn), '+/-', sem(hzvn))

np.savetxt('build/herz.txt',
    np.column_stack([t, amp, damp, f, ed, hzv, fhzv]),
    header='t\s, amp\m, damp\m, f\Hz, ed\m^3, hzv\m^3')

plt.plot(t, damp*10**3, 'kx')
plt.xlabel(r'$t\;/\;\si{\second}$')
plt.ylabel(r'$\increment h\;/\;\si{\milli\meter}$')
plt.xlim(0,21)
plt.ylim(0, 11)
plt.grid()
plt.tight_layout()
plt.savefig('build/herz.pdf')
