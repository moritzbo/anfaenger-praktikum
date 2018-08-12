import numpy as np
import matplotlib.pyplot as plt

t, U = np.genfromtxt('werte.txt', unpack=True)
t *= 1e-6  # die X-Achse
U *= 1e-3
lnu = np.log(U/928*10**3)  # unsere Y-Achse
tlnu = t*lnu
dt = t**2

mt = np.mean(t)        # x
mU = np.mean(U)
mlnu = np.mean(lnu)    # y
mtlnu = np.mean(tlnu)  # xy
mdt = np.mean(dt)      # x²
print('x mt', mt)
print('y mlnu', mlnu)
print('xy mtlnu', mtlnu)
print('x² mdt', mdt)

fmt = np.std(t, ddof=1) / np.sqrt(15)           # x
fmU = np.std(U, ddof=1) / np.sqrt(15)
fmlnu = np.std(lnu, ddof=1) / np.sqrt(15)     # y
fmtlnu = np.std(tlnu, ddof=1) / np.sqrt(15)  # xy
fmdt = np.std(dt, ddof=1) / np.sqrt(15)        # x²

b = (mlnu*mdt-mtlnu*mt)/(mdt-mt**2)
m = (mtlnu-mlnu*mt)/(mdt-mt**2)
fm = np.sqrt(
            ((1 / (fmdt-fmt**2) * fmtlnu)**2) +
            ((fmlnu * fmt / (fmdt - fmt**2))**2) +
            (((-fmlnu * (fmdt-fmt**2) + (fmtlnu - fmt * fmlnu) * 2 * fmt) / (mdt - mt**2) * fmt)**2) +
            (((fmtlnu - fmlnu * fmt) / (fmdt - fmt**2)**2 * fmdt)**2)
            )
print('m', m)
print('fm', fm)
print('b', b)
plt.plot(t, lnu, 'gx')
plt.plot(t, m*t+b, 'b-')
plt.savefig('build/ausgleichsgerade.pdf')
np.savetxt('build/rechnung.txt', np.column_stack([mt, mU, mlnu, mtlnu, mdt]), header="mt, mU, mlnu, mtlnu, mdt")
np.savetxt('build/berechnet.txt', np.column_stack([t, U, lnu, tlnu, dt]), header="t, U, lnu, tlnu, dt")
plt.clf()
