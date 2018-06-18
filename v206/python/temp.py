import numpy as np
import scipy.optimize
import uncertainties as unc
import uncertainties.unumpy as unp
from scipy import optimize
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.constants import codata

t, T1, pb, T2, pa, Leistung = np.genfromtxt("python/messwerte.txt", unpack=True)

def f(x, a, b, c):
    return a*x**2+b*x+c

def g(x, a, b):
    return -x*a/codata.value('molar gas constant')+b


pa += 1  # Umgebungsdruck
pb += 1
t *= 60   # t in s
T1 += 273.15
T2 += 273.15
R = 8.314459

params, covariance_matrix = optimize.curve_fit(f, t, T1)
errors = np.sqrt(np.diag(covariance_matrix))
print('a1 = ', params[0], '+-', errors[0])
print('b1 = ', params[1], '+-', errors[1])
print('c1 = ', params[2], '+-', errors[2])
a1 = ufloat(params[0], errors[0])
b1 = ufloat(params[1], errors[1])
c1 = ufloat(params[2], errors[2])
print('Differential300 = ', 2*300*a1+b1)
print('Differential600 = ', 2*600*a1+b1)
print('Differential900 = ', 2*900*a1+b1)
print('Differential1140 = ', 2*1140*a1+b1)
tlinspace = np.linspace(0, max(t)+300, 5000)
print('nu300 = ', (2*300*a1+b1)*(16748+660)*1/192.05)
print('nu600 = ', (2*600*a1+b1)*(16748+660)*1/192.05)
print('nu900 = ', (2*900*a1+b1)*(16748+660)*1/192.05)
print('nu1140 = ', (2*1140*a1+b1)*(16748+660)*1/192.05)
plt.plot(t, T1, 'bx', label='Messwerte von T1')
plt.plot(tlinspace, f(tlinspace, *params), 'k-', label='Ausgleichsfunktion für T2')
params, covariance_matrix = optimize.curve_fit(f, t, T2)
errors = np.sqrt(np.diag(covariance_matrix))
print('a2 = ', params[0], '+-', errors[0])
print('b2 = ', params[1], '+-', errors[1])
print('c2 = ', params[2], '+-', errors[2])

a2 = ufloat(params[0], errors[0])
b2 = ufloat(params[1], errors[1])
c2 = ufloat(params[2], errors[2])
print('Differential300 = ', 2*300*a2+b2)
print('Differential600 = ', 2*600*a2+b2)
print('Differential900 = ', 2*900*a2+b2)
print('Differential1140 = ', 2*1140*a2+b2)
plt.plot(t, T2, 'rx', label='Messwerte von T2')
plt.plot(tlinspace, f(tlinspace, *params), 'k--', label='Ausgleichsfunktion für T2')
plt.xlabel("t / s")
plt.ylabel("T / K")
plt.tight_layout()
plt.legend()
plt.grid()
plt.savefig('build/T.pdf')

plt.clf()

params, covariance_matrix = optimize.curve_fit(g, 1/T1, np.log(pb))
errors = np.sqrt(np.diag(covariance_matrix))
print('a3 = ', params[0], '+-', errors[0])
a3runden = ufloat(params[0], errors[0])
print(a3runden)
print('b3 = ', params[1], '+-', errors[1])
a3 = ufloat(params[0], errors[0])
b3 = ufloat(params[1], errors[1])

plt.plot(1/T1, np.log(pb), 'rx', label='Messwerte')
plt.plot(1/T1, g(1/T1, *params), 'k--', label='Fitfunktion')
plt.xlabel("1/T in 1/K")
plt.ylabel("ln(p warm/p0)")
plt.tight_layout()
plt.legend()
plt.grid()
plt.savefig('build/L.pdf')

plt.clf()

print('Die Verdampfungswärme zum Einsetzen hier ist jetzt')
L = a3runden*1/0.12091*1e-3  # in kJ/kg
print(L)
print('in kJ/kg')
#------------------------------- durchsatz
Qdot = (17721 + 660)*(2*t*a2+b2)
dm = Qdot/L
print('Qdot t=300s ist', Qdot[5])
print('Qdot t=600s ist', Qdot[10])
print('Qdot t=900s ist', Qdot[15])
print('Qdot t=1140s ist', Qdot[19])
print('durchsatz t=300s ist', dm[5])
print('durchsatz t=600s ist', dm[10])
print('durchsatz t=900s ist', dm[15])
print('der durchsatz t=1140s ist', dm[19])

rho0 = 5.51  # in kg/m^3
T0 = 273.15  # in kelvin
p0 = 1  # in bar
kappa = 1.14  # dim. los
d_rho = ((rho0*T0)/p0) * pa/T2
Nmech = 1/(kappa - 1) * (pb * (pa/pb)**(1/kappa) - pa) * 1/d_rho * dm *1e3 *1e-1 # in W, 1e-1 wegen bar nach Pascal

print(d_rho)
print(Nmech)

nu_id300 = T1[5]/(T1[5]-T2[5])
nu_id600 = T1[10]/(T1[10]-T2[10])
nu_id900 = T1[15]/(T1[15]-T2[15])
nu_id1140 = T1[19]/(T1[19]-T2[19])

print('ideales nu 300=', nu_id300)
print('ideales nu 600=', nu_id600)
print('ideales nu 900=', nu_id900)
print('ideales nu 1140=', nu_id1140)

print('rho t=300s ist', d_rho[5])
print('rho t=600s ist', d_rho[10])
print('rho t=900s ist', d_rho[15])
print('rho t=1140 ist', d_rho[19])
print('Nmech t=300s ist', Nmech[5])
print('Nmech t=600s ist', Nmech[10])
print('Nmech t=900s ist', Nmech[15])
print('Nmech t=1140s ist', Nmech[19])
#---------------
print("abweichungen für parameter bei 1,2.")
dA1 = 1.26e-6
dB1 = 0.001
dC1 = 0.367
dA2 = 2.46e-6
dB2 = 0.003
dC2 = 0.715
temps = [300, 600, 900, 1140]

for n in temps:
    x = np.sqrt(4*(n**2)*dA1+dB1)
    dnu = ((16748+660)/192.05)*x
    print("der fehler zu 1 (warm):", x)
    print("der relative fehler zu nu real(w) =", dnu)
for m in temps:
    y = np.sqrt(4*(m**2)*dA2+dB2)
    dmu = (16748+660)*(1/192.05)*y
    print("der fehler zu 2 (kalt):", y)
# ----------------
    dotm_fehler1 = (1/L)*np.sqrt(((-4.7)**2)*(8**2)+((-0.6)**2))
    print("fehler nur erstes m dot=", dotm_fehler1)

    dotm_fehler2 = (1/L)*np.sqrt(((-4.1)**2)*(8**2)+((-0.8)**2))
    print("fehler nur zweites m dot=", dotm_fehler2)

    dotm_fehler3 = (1/L)*np.sqrt(((-3.6)**2)*(8**2)+((-1)**2))
    print("fehler nur drittes m dot=", dotm_fehler3)

    dotm_fehler4 = (1/L)*np.sqrt(((-3.1)**2)*(8**2)+((-1.2)**2))
# ------------------
print("fehler nur viertes m dot=", dotm_fehler4)
mittel_leistung = sum(Leistung)/len(Leistung)
print(mittel_leistung)
