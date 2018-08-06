import numpy as np
import scipy.constants as const

planckh = const.Planck
cspeed = const.speed_of_light
charge = const.elementary_charge
d = 201.4*10**(-12)
ordnung = np.array([29, 29, 30, 32, 35, 37, 38, 40, 41])
ek = np.array([8.048, 8.905, 9.673 ,11.115 ,13.483 ,15.202 ,16.106 ,17.997 ,18.985])
ek = ek * charge * 10**3
rhyd = 13.6
anzahl = 9
theta = np.ones(anzahl)
sigma = np.ones(anzahl)

def ftheta(f):
    return np.arcsin((planckh*cspeed)/(2*d*f))*180/np.pi

def fsigma(f, z):
    return (z-np.sqrt(f/(rhyd*charge)))

for i in range(anzahl):
    theta[i] = ftheta(ek[i])
    sigma[i] = fsigma(ek[i], ordnung[i])

np.savetxt('build/vorbereitung.txt', np.column_stack([ordnung, ek/charge, theta, sigma]),
            header='ordnung, ek, theta, sigma')
