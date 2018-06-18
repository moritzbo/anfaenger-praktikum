import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import sem

t, t1, t2, t5, t6 = np.genfromtxt('python/dynamisch.txt', unpack=True)
plt.plot(2*t-2, t1, 'ro', markersize=1, label=r'$T_1$')
plt.plot(2*t-2, t2, 'ko', markersize=1, label=r'$T_2$')
plt.legend()
plt.grid()
plt.xlabel(r'$t\:/\:\si{\second}$')
plt.ylabel(r'$T\:/\:\si{\celsius}$')
plt.xlim(0, 885)
plt.ylim(25, 70)
plt.tight_layout(pad=0)
plt.savefig('build/messing.pdf', bbox_inches='tight', pad_inches=0)
plt.clf()

plt.plot(2*t-2, t5, 'bo', markersize=1, label=r'$T_5$')
plt.plot(2*t-2, t6, 'go', markersize=1, label=r'$T_6$')
plt.legend()
plt.grid()
plt.xlabel(r'$t\:/\:\si{\second}$')
plt.ylabel(r'$T\:/\:\si{\celsius}$')
plt.xlim(0, 885)
plt.ylim(22, 77)
plt.tight_layout(pad=0)
plt.savefig('build/aluminium.pdf', bbox_inches='tight', pad_inches=0)
plt.clf()

maxt1 = np.array([36*2, 73*2, 112*2, 151*2, 191*2, 230*2, 270*2, 310*2, 350*2, 390*2, 429*2])
max1 = np.array([34.00, 39.75, 44.21, 47.72, 50.63, 53.10, 55.20, 56.82, 58.53, 59.97, 61.21])
mint1 = np.array([45*2, 86*2, 127*2, 167*2, 207*2, 247*2, 287*2, 328*2, 368*2, 408*2, 0])
min1 = np.array([33.75, 39.05, 43.13, 46.38, 49.08, 51.39, 53.36, 54.93, 56.53, 57.88, 0])
maxt2 = np.array([23*2, 63*2, 103*2, 143*2, 183*2, 223*2, 263*2, 303*2, 343*2, 383*2, 423*2])
max2 = np.array([41.86, 47.67, 52.03, 55.38, 58.23, 60.72, 62.80, 64.20, 66.10, 67.62, 68.85])
mint2 = np.array([42*2, 82*2, 123*2, 163*2, 203*2, 243*2, 283*2, 323*2, 363*2, 403*2, 0])
min2 = np.array([35.43, 40.43, 44.25, 47.36, 50.06, 52.34, 54.30, 55.89, 57.54, 58.89, 0])

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
    phi.append(2*np.pi*(maxt1[i]-maxt2[i])/80)
    if amplitude1[i] == 0 or amplitude2[i] == 0 or amplitude1[i] == amplitude2[i]:
        kappa.append(0)
    else:
        kappa.append((8520*385*0.03**2)/(2*(maxt1[i]-maxt2[i])*np.log(amplitude2[i]/amplitude1[i])))
    i += 1
kappa1 = []
i = 0
while i < len(kappa):
    if kappa[i] == 0:
        i += 1
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
print('Messing')
print('kappa', np.mean(kappa1), sem(kappa1))
print('phi', np.mean(phi1), sem(phi1))
np.savetxt('build/messingminmax.txt', np.column_stack([maxt1, max1, mint1, min1, amplitude1, maxt2, max2, mint2, min2, amplitude2, phi, kappa]), header='1tmax max tmin min amplitude | 2tmax max tmin min amplitude | phi kappa')

maxt1 = np.array([28*2, 66*2, 106*2, 146*2, 186*2, 226*2, 266*2, 306*2, 346*2, 386*2, 426*2])
max1 = np.array([40.23, 47.78, 52.37, 55.53, 58.08, 60.31, 62.19, 63.47, 65.15, 66.52, 67.69])
mint1 = np.array([44*2, 84*2, 125*2, 165*2, 205*2, 245*2, 285*2, 325*2, 365*2, 405*2, 0])
min1 = np.array([37.55, 43.48, 47.33, 50.21, 52.61, 54.71, 56.48, 57.84, 59.37, 60.65, 0])
maxt2 = np.array([22*2, 62*2, 102*2, 142*2, 182*2, 222*2, 262*2, 302*2, 342*2, 382*2, 422*2])
max2 = np.array([46.97, 54.08, 58.45, 61.49, 64.02, 66.25, 68.14, 69.28, 71.15, 72.52, 73.67])
mint2 = np.array([42*2, 82*2, 122*2, 162*2, 202*2, 242*2, 282*2, 322*2, 362*2, 402*2, 0])
min2 = np.array([37.09, 42.59, 46.23, 49.06, 51.49, 53.61, 55.41, 56.84, 58.39, 59.67, 0])

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
    phi.append(2*np.pi*(maxt1[i]-maxt2[i])/80)
    if amplitude1[i] == 0 or amplitude2[i] == 0 or amplitude1[i] == amplitude2[i]:
        kappa.append(0)
    else:
        kappa.append((2800*830*0.03**2)/(2*(maxt1[i]-maxt2[i])*np.log(amplitude2[i]/amplitude1[i])))
    i += 1
kappa1 = []
i = 0
while i < len(kappa):
    if kappa[i] == 0:
        i += 1
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
print('Aluminium')
print('kappa', np.mean(kappa1), sem(kappa1))
print('phi', np.mean(phi1), sem(phi1))
np.savetxt('build/aluminiumminmax.txt', np.column_stack([maxt1, max1, mint1, min1, amplitude1, maxt2, max2, mint2, min2, amplitude2, phi, kappa]), header='1tmax max tmin min amplitude | 2tmax max tmin min amplitude | phi kappa')

print('f Messing', 1/80)
print('f Edelstahl', 1/200)
print('λ Messing', 2*80*np.sqrt((np.pi*90)/(80*8520*385)))
print('λ Aluminium', 2*80*np.sqrt((np.pi*220)/(80*2800*830)))
print('λ Edelstahl', 2*200*np.sqrt((np.pi*21)/(200*8000*400)))
