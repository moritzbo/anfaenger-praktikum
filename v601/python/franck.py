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
laenge = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,20.9])
abstand = np.array([22, 21.5, 21, 22, 20, 22, 20, 21, 21, 21])
mittelwert = np.mean(abstand)
mittelfehler = sem(abstand)
skalierung = ufloat(mittelwert, mittelfehler)
skalierung = (5/skalierung)*10
print("skalierung in x mit fehler:", skalierung)
skalierung = unp.nominal_values(skalierung)
print("mittelwert:", mittelwert)
print("fehler des mittelwerts:", mittelfehler)

Maxima_x = np.array([5.3, 7.4, 9.6, 11.8, 14.45, 16.35, 18.85])  # lage der maxima in cm
Maxima_scale = Maxima_x*skalierung  # lage der maxima in volt
print("------------frack hertz; totaler abstand der maxima-----------")
tot1 = (Maxima_scale[1]-Maxima_scale[0])
tot2 = (Maxima_scale[2]-Maxima_scale[0])/2
tot3 = (Maxima_scale[3]-Maxima_scale[0])/3
tot4 = (Maxima_scale[4]-Maxima_scale[0])/4
tot5 = (Maxima_scale[5]-Maxima_scale[0])/5
tot6 = (Maxima_scale[6]-Maxima_scale[0])/6
toti = [tot1, tot2, tot3, tot4, tot5, tot6]
mitteltot = sum(toti)/len(toti)
print("totale abstandswerte", toti)
print("mittelwert des tot. abstandes", mitteltot)

print("-----------FH; abstand benachbarter punkte--------")
d1 = (Maxima_scale[1]-Maxima_scale[0])
d2 = (Maxima_scale[2]-Maxima_scale[1])
d3 = (Maxima_scale[3]-Maxima_scale[2])
d4 = (Maxima_scale[4]-Maxima_scale[3])
d5 = (Maxima_scale[5]-Maxima_scale[4])
d6 = (Maxima_scale[6]-Maxima_scale[5])
di = [d1, d2, d3, d4, d5, d6]
mitteld = sum(di)/len(di)
print("abstand je zwei benachbarter maxima", di)
print("Mittelwert 2er", mitteld)

print("-----------wellenlänge und anregungsenergien-----------------")
h = const.Planck
c = const.speed_of_light
q = const.elementary_charge

for m in di:
    (h*c)/(q*m)

for n in toti:
    (h*c)/(q*n)


λ_di = np.array([2.48e-7, 2.37e-7, 2.37e-7, 1.97e-7, 2.74e-7, 2.08e-7])
λ_toti = np.array([2.48e-7, 2.42e-7, 2.40e-7, 2.28e-7, 2.36e-7, 2.31e-7])
En_di = np.array([4.99, 5.23, 5.23, 6.29, 4.52, 5.96])
En_toti = np.array([4.99, 5.12, 5.16, 5.44, 5.25, 5.37])
print("Mittelwert von λ_di", np.mean(λ_di))
print("Mittelwert von λ_toti", np.mean(λ_toti))
print("Mittelwert von En_di", np.mean(En_di))
print("Mittelwert von En_toti", np.mean(En_toti))

for y in λ_di:
    ((h*c)/y)/q
    y += 1

for z in λ_toti:
    ((h*c)/z)/q
    z += 1
#----------------------
np.savetxt('werte.txt', np.column_stack([λ_di, En_di, λ_toti, En_toti]), header="λ_di En_di λ_toti En_toti")
with open('werte.txt', 'r') as f:
    print(f.read())

print("standartabweichung λ_di", sem(λ_di))
print("standartabweichung λ_toti", sem(λ_toti))
print("standartabweichung En_d", sem(En_di))
print("standartabweichung En_tot", sem(En_toti))
