import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy import optimize
from scipy.stats import sem

print("------------Messung der schallgeschwindigkeit------------")
t1 = 30.1e-6  # t1 in sekunden
t2 = 59.2e-6  # t2 in sekunden
A1 = 1.2  # Amplitude in volt
A2 = 0.15  # auch in volt
c_lit = 2730  # m/s

dt = t2 - t1
h_mess = 3.97e-2 # gemessene höhe in meter
c_schall = (2*h_mess)/dt
print("c_schall in acryl:", c_schall, "m/s")

h_tief = 41e-3  # höhe mit tiefenmessung in meter
print("mit tiefenmessung:", (2*h_tief)/dt)
dproz = ((np.abs(h_tief - h_mess))/h_mess)*100
print("prozentuale abweichung der längen:", dproz, "prozent")

t, v, hf, db = np.genfromtxt('python/daten/programm/Messung-1.txt', unpack=True)
plt.plot(t, v, 'b.', markersize=2, label='Messwerte')
plt.plot([t1*10**6, t1*10**6], [0, 1.5], 'r-', linewidth=0.5, label='1. Peak')
plt.plot([t2*10**6, t2*10**6], [0, 1.5], 'g-', linewidth=0.5, label='2. Peak')
plt.xlabel(r'$t\;/\;\si{\micro\second}$')
plt.ylabel(r'$U\;/\;\si{\volt}$')
plt.xlim(-1, 101)
plt.ylim(0, 1.5)
plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig('build/acrylschall.pdf')

plt.clf()
print("----------bestimmung der dämpfung-------------")

h_mess, U1, U2, t, H_schieb = np.genfromtxt('python/daten/daempfung.txt', unpack=True)

h_mess *= 1e-3  # h in meter
t *= 1e-6  # t in sek
H_schieb *= 1e-3  # in meter
c_aq = 1500  # m/s
ρ_aq = 1  # g/cm^3
c_acryl = c_lit  # m/s
ρ_acryl = 1.18  # g/cm^3

len = len(H_schieb)
absorp = np.linspace(0, len-1, len)
absorp1 = np.linspace(0, len-1, len)
i = 0
while i < len:
    absorp[i] = np.log(U1[i]/U2[i])/(2*H_schieb[i])
    absorp1[i] = np.log(U1[i]/U2[i])/(2*h_mess[i])
    i += 1
np.savetxt('build/absorption.txt',
        np.column_stack([U1, U2, H_schieb, absorp, h_mess, absorp1]),
        header='U1, U2, H_schieb, absrop, h_mess, absorp1')
