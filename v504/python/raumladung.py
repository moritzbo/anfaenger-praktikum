import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy import optimize
import scipy.constants as const
import uncertainties.unumpy as unp

me = const.electron_mass
de = const.epsilon_0
le = const.elementary_charge
kbolt = const.Boltzmann
a = 0.03

v25, a25 = np.genfromtxt('python/25a.txt', unpack=True)
vn, an = np.genfromtxt('python/nano.txt', unpack=True)
vnk=vn+an*10**(-9)*10**3
ank=np.log(an)
vnk=-vnk
vn=-vn

# Fit für den linearen Anlaufstromlogarithmus
def f(k, m, b):
    return m*k+b
params, covariance_matrix = optimize.curve_fit(f, vnk, ank)
errors = np.sqrt(np.diag(covariance_matrix))
mf = ufloat(params[0], errors[0])
bf = ufloat(params[1], errors[1])
print('Steigung:',mf,params[0], errors[0])
print('Abschnitt:',bf,params[1], errors[1])

# Damit weiterrechnen
print('T = ',le/(kbolt*mf))

x=np.linspace(-1.05,0)
# Anlaufstrom
plt.subplot(1,2,1)
plt.title('Anlaufstrom')
plt.plot(vnk,ank,'kx',label='Messwerte')
plt.plot(x,f(x,unp.nominal_values(mf),unp.nominal_values(bf)),'r-',label='Theoriekurve')
plt.xlabel(r'$U\:/\:\si{\volt}$')
plt.ylabel(r'$\ln(I)\:/\:\ln(\si{\nano\ampere})$')
plt.xlim(-1.05,0)
plt.ylim(0,5.5)
plt.tight_layout()
plt.legend()
plt.grid()

# Raumladungsdichte
# Fit für den Exponenten
def f(k, m):
    return (4/9*de*np.sqrt(2*le/me)*(k**m)/a**2)
params, covariance_matrix = optimize.curve_fit(f, v25, a25)
errors = np.sqrt(np.diag(covariance_matrix))
ul = ufloat(params[0], errors[0])
print('Exponent:',params[0], errors[0])
print(ul)
l=params[0]

# Plot
x = np.linspace(0,80)
plt.subplot(1,2,2)
plt.title('Raumladungsdichte')
plt.plot(v25,a25,'kx',label='Messwerte')
plt.plot(x,f(x,l),'r-',label='Theoriekurve')
plt.xlabel(r'$U\:/\:\si{\volt}$')
plt.ylabel(r'$I\:/\:\si{\milli\ampere}$')
plt.xlim(0,80)
plt.ylim(0,1.9)
plt.tight_layout()
plt.grid()
plt.legend()
plt.savefig('build/25a.pdf')
plt.clf()

def umspeichern(a):
    i=0
    b=np.zeros(16)
    while i < len(a):
        b[i]=a[i]
        i=i+1
    return b

vn1=umspeichern(vn)
vnk1=umspeichern(vnk)
an1=umspeichern(an)
ank1=umspeichern(ank)
np.savetxt('build/nano.txt',np.column_stack([vn1,vnk1,an1,ank1,v25,a25]),header='vn,vnk,an,ank,v25,a25')
