import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
import uncertainties.unumpy as unp
from scipy import optimize
from scipy.stats import sem

h, amp, HF, TGC = np.genfromtxt('python/daten/programm/auge1.Txt', unpack=True)

max1 = amp[:20]
max2 = amp[35:]
max3 = amp[180:]
max4 = amp[240:]
print("Maximum Values: ", np.argmax(max1), max(max1))
print("maximal values:", np.argmax(max2), max(max2))
print("maximal values:", np.argmax(max3), max(max3))
print("maximal values:", np.argmax(max4), max(max4))
print(h[18])
print(h[167])
print(h[233])
print(h[725])

plt.plot(h, amp, 'k.', markersize=3, label='Messwerte')
plt.xlabel(r"$h\;/\;\si{\milli\meter}$")
plt.ylabel(r"$U\;/\;\si{\volt}$")
plt.xlim(-2, 138)
plt.ylim(-0.05, 1.5)
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig('build/auge1.pdf')

plt.clf()

np.savetxt('build/augwert.txt', np.column_stack([h, amp]), header='h amp')
