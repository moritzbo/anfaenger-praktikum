import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy import optimize
import scipy.constants as const
import uncertainties.unumpy as unp

N = np.genfromtxt("python/rhodium.txt", unpack=True)
fehler = 13
lenN = len(N)
t = np.linspace(1, lenN, lenN)
t *= 20
N -= -fehler
fehlerN = np.sqrt(N)
Nlog = np.log(N)
fehlerNlog = (fehlerN)/N
print("------------lange Halbwertszeit----------")
lNlog = Nlog[8:]
lfehlerNlog = fehlerNlog[8:]
tr_k = t[8:]


def longfit(x, m, b):
    return m*x + b


tr = np.linspace(110, 750)
paramsr, covariance_matrix = optimize.curve_fit(longfit, tr_k, lNlog)
errorsr = np.sqrt(np.diag(covariance_matrix))

m = ufloat(paramsr[0], errorsr[0])
b = ufloat(paramsr[1], errorsr[1])
print('Steigung m =', m)
print('Abschnitt b =', b)

plt.errorbar(tr_k, lNlog, xerr=None, yerr=lfehlerNlog, fmt='kx', markersize=5, label='Messwerte mit Fehler, lange T')
plt.plot(tr, longfit(tr, *paramsr), "r--", label="Fit der langen T")

print("Halbwertszeiten: Rhodium")
Th_Rh_lang = np.log(2)/0.00286
print("Halbwertszeit von Rh lange Th:", Th_Rh_lang)

print("--------kurze halbwertszeit---------")

# lange Messzeitwerte
lmw = np.exp(paramsr[1]+paramsr[0]*t)
fehlerlmw = np.sqrt(lmw)
lmwlog = np.log(lmw)
fehlerlmwlog = (fehlerlmw)/lmw

kmw = N - lmw

kmw = kmw[:8]
fehlerkmw = np.sqrt(kmw)
kmwlog = np.log(kmw)
fehlerkmwlog = (fehlerkmw)/kmw

tl = t[:8]


def shortfit(x, s, q):
    return s*x + q


tl_l = np.linspace(0, 180)
paramsl, covariance_matrix = optimize.curve_fit(shortfit, tl, kmwlog)
errorsl = np.sqrt(np.diag(covariance_matrix))

s = ufloat(paramsl[0], errorsl[0])
q = ufloat(paramsl[1], errorsl[1])
print('Steigung s =', s)
print('Abschnitt q =', q)


plt.errorbar(tl, kmwlog, xerr=None, yerr=fehlerkmwlog, fmt='bx', markersize=5, label="Messwerte mit Fehler, kurze T")
plt.plot(tl_l, shortfit(tl_l, *paramsl), "k--", label="Fit der kurzen T")
plt.grid()
plt.xlim(0, 750)
plt.ylim(2.9, 7.5)
plt.xlabel(r"$t\;/\;\si{\second}$")
plt.ylabel(r"$\log(N)$")
plt.legend()
plt.savefig("build/shortfit.pdf")
plt.clf()

print("originaldaten mit summenkurve")
tsum = np.linspace(0, 750, 1000)
Efr = np.exp(paramsr[1]+paramsr[0]*tsum)
Efl = np.exp(paramsl[1]+paramsl[0]*tsum)
Efkt = (Efr + Efl)
plt.plot(tsum, Efkt, "g-", label="Summenkurve")
plt.errorbar(t, N, xerr=None, yerr=fehlerN, fmt="k.", label="Messwerte")
plt.plot([160, 160], [0, 1800], 'b-', label='Approximale Grenze beider Zerfälle')
plt.grid()
plt.xlim(0, 750)
plt.ylim(0, 1800)
plt.xlabel(r"$t\;/\;\si{\second}$")
plt.ylabel(r"$N\;/\;\text{Anzahl}$")
plt.legend()
plt.savefig("build/Rhodium.pdf")
plt.clf()

mw = np.linspace(1, lenN, lenN) # [kmw, lmw]
fehlermw = np.linspace(1, lenN, lenN) # [fehlerkmw, fehlerlmw]
mwlog = np.linspace(1, lenN, lenN) # [kmwlog, lmwlog]
fehlermwlog = np.linspace(1, lenN, lenN) # [fehlerkmwlog, fehlerlmwlog]

for i in range(8):
    mw[i] = kmw[i]
    fehlermw[i] = fehlerkmw[i]
    mwlog[i] = kmwlog[i]
    fehlermwlog[i] = fehlerkmwlog[i]
for i in range(8, 36):
    mw[i] = lmw[i]
    fehlermw[i] = fehlerlmw[i]
    mwlog[i] = lmwlog[i]
    fehlermwlog[i] = fehlerlmwlog[i]

np.savetxt('build/rhodium.txt',
    np.column_stack([t, N, fehlerN, Nlog, fehlerNlog, mw, fehlermw, mwlog, fehlermwlog]),
    header='t, N, fehlerN, Nlog, fehlerNlog, mw, fehlermw, mwlog, fehlermwlog')

# s kurz, m lang
tk = -np.log(2)/s
print("Halbwertszeit von Rhodium, kurz:", tk, 's')
# tk /= 60
# print("Halbwertszeit von Rhodium, kurz:", tk, 'min')
lit = 42.3
prfe = 100*abs(lit-unp.nominal_values(tk))/lit
print('proz fehler', prfe)

tl = -np.log(2)/m
print("Halbwertszeit von Rhodium, lang:", tl, 's')
tl /= 60
print("Halbwertszeit von Rhodium, lang:", tl, 'min')
lit = 4.3
prfe = 100*abs(lit-unp.nominal_values(tl))/lit
print('proz fehler', prfe)
