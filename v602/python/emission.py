import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as const
from scipy.stats import sem

h = const.Planck
c = const.speed_of_light
q = const.elementary_charge
d = 201.4*10**(-12) #m
u = 35*10**3 #eV
thetamin = 5*np.pi/180

lmint = (h*c)/(q*u)
print('Theorie lmin', lmint)
lmin = 2*d*np.sin(thetamin)
print('Messung lmin', lmin)

print('e0 U= ', (h*c)/(q*2*d*np.sin(thetamin)))

theta, impuls = np.genfromtxt('python/emission.txt', unpack=True)

plt.plot(theta/2, impuls, 'b.')
plt.xlabel(r'$θ\;/\;\si{\degree}$')
plt.ylabel('Counts')
plt.xlim(3.5, 26.5)
plt.ylim(0, 4320)
plt.grid()
plt.tight_layout()
plt.savefig('build/emission.pdf')
plt.clf()

plt.plot(theta/2, impuls, 'b.')
plt.xlabel(r'$θ\;/\;\si{\degree}$')
plt.ylabel(r'$\log(\text{Counts})$')
plt.yscale('log')
plt.xlim(3.5, 26.5)
plt.grid()
plt.tight_layout()
plt.savefig('build/emissionlog.pdf')

def energie(phi):
    phi = phi * np.pi/180
    return (h*c)/(2*d*q*np.sin(phi))

print('linker peak')
x1 = 39.5/2
y1 = 313
x2 = 40/2
y2 = 1363
m = (y2-y1)/(x2-x1)
b = y2 - x2 * m
x3 = (1455/2-b)/m
print('x3',x3)
print('E3',energie(x3))

x1 = 40.4/2
y1 = 1455
x2 = 40.8/2
y2 = 372
m = (y2-y1)/(x2-x1)
b = y2 - x2 * m
x4 = (1455/2-b)/m
print('x4',x4)
print('E4',energie(x4))

print('delta E',energie(x3)-energie(x4))
deltae = [energie(x3)-energie(x4), 1]

print('rechter peak')
x1 = 44/2
y1 = 352
x2 = 44.4/2
y2 = 4304
m = (y2-y1)/(x2-x1)
b = y2 - x2 * m
x3 = (4304/2-b)/m
print('x3', x3)
print('E3', energie(x3))

x1 = 45.2/2
y1 = 3946
x2 = 45.5/2
y2 = 268
m = (y2-y1)/(x2-x1)
b = y1 - x1 * m
x4 = (4304/2-b)/m
print('x4',x4)
print('E4',energie(x4))

print('delta E', energie(x3)-energie(x4))
deltae[1] = energie(x3)-energie(x4)
print('mean=', np.mean(deltae))
print('sem=', sem(deltae))
