import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import sem

t, t7, t8, T = np.genfromtxt('python/edelstahl.txt', unpack=True)
plt.plot(2*t-2, t7, 'ro', markersize=1, label=r'$T_7$')
plt.plot(2*t-2, t8, 'ko', markersize=1, label=r'$T_8$')
plt.legend()
plt.grid()
plt.xlabel(r'$t\:/\:\si{\second}$')
plt.ylabel(r'$T\:/\:\si{\celsius}$')
plt.xlim(0, 1005)
plt.ylim(25, 70)
plt.tight_layout(pad=0)
plt.savefig('build/edelstahl.pdf', bbox_inches='tight', pad_inches=0)
plt.clf()

maxt1 = np.array([47*2, 156*2, 256*2, 356*2, 456*2])
max1 = np.array([50.04, 57.61, 61.88, 65.00, 67.49])
mint1 = np.array([104*2, 205*2, 305*2, 405*2, 0])
min1 = np.array([38.52, 44.72, 48.41, 51.24, 0])
maxt2 = np.array([97*2, 197*2, 292*2, 387*2, 485*2])
max2 = np.array([33.05, 38.59, 42.73, 45.95, 48.46])
mint2 = np.array([112*2, 218*2, 321*2, 423*2, 0])
min2 = np.array([33.03, 38.38, 42.22, 45.19, 0])

ampl1 = []
i = 0
while i < len(max1)-1:
    ampl1.append(max1[i]-min1[i])
    ampl1.append(max1[i+1]-min1[i])
    i += 1
amplitude1 = []
i = 0
while i < len(ampl1):
    amplitude1.append((ampl1[i] + ampl1[i+1])/4)
    i += 2
amplitude1.append(0)
ampl2 = []
i = 0
while i < len(max2)-1:
    ampl2.append(max2[i]-min2[i])
    ampl2.append(max2[i+1]-min2[i])
    i += 1
amplitude2 = []
i = 0
while i < len(ampl2):
    amplitude2.append((ampl2[i] + ampl2[i+1])/4)
    i += 2
amplitude2.append(0)
kappa = []
phi = []
i = 0
while i < len(max1):
    phi.append(2*np.pi*(maxt2[i]-maxt1[i])/200)
    if amplitude1[i] == 0 or amplitude2[i] == 0 or amplitude1[i] == amplitude2[i]:
        kappa.append(0)
    else:
        kappa.append((8000*400*0.03**2)/(2*(mint2[i]-mint1[i])*np.log(amplitude1[i]/amplitude2[i])))
    i += 1
kappa1 = []
i = 0
while i < len(kappa):
    if kappa[i] == 0:
        i += 1
    else:
        if kappa[i] < 0:
            kappa1.append(-kappa[i])
        else:
            kappa1.append(kappa[i])
        i += 1
phi1 = []
i = 0
while i < len(phi)-1:
    if phi[i] == 0:
        i += 1
    else:
        if phi[i] < 0:
            phi1.append(-phi[i])
        else:
            phi1.append(phi[i])
        i += 1
print('Edelstahl')
print('kappa', np.mean(kappa1), sem(kappa1))
print('phi', np.mean(phi1), sem(phi1))
np.savetxt('build/edelstahlminmax.txt', np.column_stack([maxt1, max1, mint1, min1, amplitude1, maxt2, max2, mint2, min2, amplitude2, phi, kappa]), header='7tmax max tmin min amplitude | 8tmax max tmin min amplitude | phi kappa')
