import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
import uncertainties.unumpy as unp
from scipy import optimize
import scipy.constants as const
from scipy.stats import sem

h = const.Planck
c = const.speed_of_light
q = const.elementary_charge

# scale
laenge = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,16.8])  # in cm
abstand = np.array([24, 26, 24, 25, 21.5, 25.5, 24.5])  # laenge der intervalle in mm
mittelwert = np.mean(abstand)
mittelfehler = sem(abstand)
skalierung = ufloat(mittelwert, mittelfehler)
skalierung = (5/skalierung)*10  #skalierung pro 5 volt in cm jetzt
print("skalierung in x mit fehler:", skalierung)
skalierung = unp.nominal_values(skalierung)
print("mittelwert:", mittelwert)
print("fehler des mittelwerts:", mittelfehler)

null_zu_tangente = 10.2  # in cm
null_zu_tangente = null_zu_tangente*skalierung  # Ionisierungsspannung in volt
print("ionisierungsspannung + K:", null_zu_tangente)
K = 2.725  # in volt
Ionspannung = null_zu_tangente - K  # finale ionspannung in volt
print("Ionspannung:", Ionspannung)
