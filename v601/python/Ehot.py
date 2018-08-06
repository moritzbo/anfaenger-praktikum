import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
import uncertainties.unumpy as unp
from scipy import optimize
import scipy.constants as const
from scipy.stats import sem
from pylab import fill

h = const.Planck
c = const.speed_of_light
q = const.elementary_charge
# scal1 = 0.41  # Volt pro centimeter in [0,2]
# scal2 = 0.43  # Volt pro centimeterin [2,10]
U1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

abstand = np.array([49, 50.5, 48, 50, 49.5])  # abstand der intervalle in mm
mittelwert = np.mean(abstand)
print("Mittelwert:", mittelwert)
mittelwert_fehler = sem(abstand)
print("Mittelfehler:", mittelwert_fehler)
skalierung = ufloat(mittelwert, mittelwert_fehler)
skalierung = (2/skalierung)*10
print("skalierung mit fehler:", skalierung)
skalierung = unp.nominal_values(skalierung)

u1 = U1*skalierung  # x scale
u_ges = u1

print("bestimmung der steigung")

y_skalierung = 1/13  # bestimmt durch max ausschlag = 1 und höhe = 13 cm
print("y skalierung:", y_skalierung)
y_werte = np.array([13,11.3,9.6,7.95,6.2,4.6,3.1,1.8,0.8,0.3,0,0])  # in cm
y_anwend = y_skalierung*y_werte

steigung = np.array([0.323,0.323,0.314,0.332,0.304,0.285,0.247,0.190,0.095,0.057,0,0])

plt.plot(u_ges, steigung, "rx", label="integrale Energieverteilung")
# plt.plot([8.405, 8.405], [0, 1.5], 'k--', label="Kontaktpotential")
# plt.plot([11, 11], [0, 1.5], 'k--', label='"')
# fill([8.405, 11, 11, 8.405], [0, 0, 1.5, 1.5], "b", alpha=0.15, edgecolor="b")
plt.plot([3.348, 3.348], [0, 0.4], 'k--', label=r'$U_\text{max}$')
plt.xlabel(r"$U_A\;/\;\si{\volt}$")
plt.ylabel("Steigung")
# plt.ylim(-0.1, 1.5)
# plt.xlim(0, 12)
plt.legend()
plt.grid()
plt.savefig("build/intE-153.pdf")
plt.clf()

print("--------Kontaktpotential----------")

np.savetxt('python/153werte.txt', np.column_stack([u_ges, steigung]), header="u_ges steigung")
with open('python/153werte.txt', 'r') as f:
    (f.read())
