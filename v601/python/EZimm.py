import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
import uncertainties.unumpy as unp
from scipy import optimize
import scipy.constants as const
from scipy import stats
from scipy.stats import sem
from pylab import fill

h = const.Planck
c = const.speed_of_light
q = const.elementary_charge
# scal2 = 0.41  # Volt pro centimeterin [2,10]
abstand = np.array([48, 48.5, 48.5, 48, 49.5])  # abstand der punkte zueindander
mittelwert = np.mean(abstand)

mittelwert_fehler = sem(abstand)
skalierung = ufloat(mittelwert, mittelwert_fehler)
skalierung = (2/skalierung)*10
print("skalierung in x:", skalierung)
skalierung = unp.nominal_values(skalierung)
print("fehler des mittelwerts:", mittelwert_fehler)
print("mittelwert:", mittelwert)

UA2 = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,20.5,21,21.5,22,23,24,25])
ua2 = UA2*skalierung
ua_ges = ua2
# print("U max:", ua2[19])
y_skalierung = 1/15.3  # bestimmt durch max ausschlag = 1 und höhe = 15.1 cm
print("y skalierung:", y_skalierung)
y_werte = np.array([15.3, 15, 14.7, 14.4, 14, 13.6, 13.25, 12.85, 12.4, 11.9, 11.4, 10.9, 10.3, 9.65, 8.9, 8.1, 7.25, 6.25, 5, 3.5, 1.6, 0.7, 0.3, 0.1, 0,0,0])  # in cm
y_anwend = y_skalierung*y_werte

# print("steigung")
# i = 0
# while i < len(y_anwend):
#      print((y_anwend[i] - y_anwend[i+1])/skalierung)
#      i = i + 1
#      if i == 28:
#              break

# incline array ist die liste der steigugswerte
incline = np.array([0.4754901960784297
,0.4754901960784324
,0.4754901960784297
,0.6339869281045756
,0.6339869281045756
,0.554738562091504
,0.6339869281045756
,0.7132352941176445
,0.7924836601307216
,0.7924836601307188
,0.7924836601307188
,0.950980392156862
,1.0302287581699336
,1.1887254901960795
,1.2679738562091512
,1.3472222222222214
,1.5849673202614376
,1.9812091503267986
,2.3774509803921564
,3.011437908496732
,1.4264705882352946
,0.6339869281045751
,0.31699346405228757
,0.1584967320261438
,0
,0
,0])

plt.plot(ua_ges, incline, "rx", label="differentielle Energieverteilung")
plt.plot([8.247, 8.247], [0, 3], 'k--', label="Kontaktpotential")
plt.plot([11, 11], [0, 3], 'k--')
fill([8.247, 11, 11, 8.247], [0, 0, 3, 3], "b", alpha=0.15, edgecolor="b")
plt.xlabel(r"$U_A\;/\;\si{\volt}$")
plt.ylabel("Steigung")
# plt.ylim(-0.1, 1.5)
# plt.xlim(0, 12)
plt.legend()
plt.grid()
plt.savefig("build/Energieverteilung.pdf")
plt.clf()

print("--------Kontaktpotential----------")
maximum_indices = np.where(incline == max(incline))
print(maximum_indices)
K = 11 - ua2[19]
print("Kontaktpotential:", K)

np.savetxt('python/zimmwerte.txt', np.column_stack([ua_ges, incline]), header="ua_ges incline")
with open('python/zimmwerte.txt', 'r') as f:
    f.read()
