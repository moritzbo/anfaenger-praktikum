import numpy as np
import scipy.optimize
import uncertainties as unc
import uncertainties.unumpy as unp
from scipy import optimize
import matplotlib.pyplot as plt
from uncertainties import ufloat


def f(x, a, b):
    return a*x+b


# Anfang einseitige Einspannung und runder Querschnitt
xr, Dr, DrG = np.genfromtxt('python/stange1rund.txt', unpack=True)
# in cm, mm, mm
m = 1.143  # in kg
L = 0.50  # in m von 0.6 auf 0.5 geändert, da wir nur das gebogen haben
xr *= 1e-2  # x1 jetzt in m
d = 10  # Durchmesser d des Stabs in mm
d *= 1e-3  # d jetzt in m
I = (np.pi/4)*((d/2)**4)  # Flaechentraegheitsmoment für runden Querschnitt  in m^4

D = DrG-Dr  # Die Ausgleichsrechnung, um die Biegung in Nullage zu beachten
xwerte = L*(xr**2)-(xr**3)/3  # Die Gleichung für einseitige Einspannung
xwerte *= 1e3  # um auf der x-Achse mm zu haben
params, covariance_matrix = optimize.curve_fit(f, xwerte, D)
errors = np.sqrt(np.diag(covariance_matrix))
print('a =', params[0], '+-', errors[0])
print('b =', params[1], '+-', errors[1])

a = ufloat(params[0], errors[0])

print('E/10^9 fuer rund, einseitige Einspannung ist', (m*9.81)/(2*I*a)*1e-9)

plt.plot(xwerte, D, 'gx', label='gemessene Werte')
plt.plot(xwerte, f(xwerte, *params), 'b-', label='fit funktion')
plt.title('Runder Stab mit einseitiger Einspannung')
plt.legend()
plt.grid()
plt.xlabel(r'$(Lx^2-\frac{x^3}{3})/$mm³')
plt.ylabel('D(x)/mm')
plt.tight_layout()
plt.savefig('build/rundeinseitig.pdf')
plt.clf()
# Ende einseitige Einspannung und runder Querschnitt

# Anfang einseitige Einspannung und quadratischer Querschnitt
xe, De, DeG = np.genfromtxt('python/stange1eckig.txt', unpack=True)
# in cm, mm, mm
m = 2.9605  # in kg
L = 0.50  # in m, ebenfalls von 0.6 auf 0.5 ggeändert
xe *= 1e-2  # x1 jetzt in m
a = 10  # Seitenlaenge a in mm
b = 12  # Seitenlaenge b in mm
a *= 1e-3  # a jetzt in m
b *= 1e-3  # b in m
I = (b**3)*a/12  # Flaechentraegheitsmoment für einen quadratischen Querschnitt in m^4
D = DeG-De  # Die Ausgleichsrechnung, um die Biegung in Nullage zu beachten

xwerte = L*(xe**2)-(xe**3)/3  # Die Gleichung für einseitige Einspannung
xwerte *= 1e3  # um auf der x-Achse mm zu haben
params, covariance_matrix = optimize.curve_fit(f, xwerte, D)
errors = np.sqrt(np.diag(covariance_matrix))
print('a =', params[0], '+-', errors[0])
print('b =', params[1], '+-', errors[1])

a = ufloat(params[0], errors[0])

print('E/10^9 fuer eckig, einseitige Einspannung ist', (m*9.81)/(2*I*a)*1e-9)

plt.plot(xwerte, D, 'rx', label='Messwerte')
plt.plot(xwerte, f(xwerte, *params), 'b-', label='fit')
plt.title('Eckiger Stab mit einseitiger Einspannung')
plt.legend()
plt.grid()
plt.xlabel(r'$(Lx^2-\frac{x^3}{3})/$mm³')
plt.ylabel('D(x)/mm')
plt.tight_layout()
plt.savefig('build/quadrateinseitig.pdf')
plt.clf()
# Ende einseitige Einspannung und quadratischer Querschnitt

# Anfang zweiseitige Einspannung und quadratischer Querschnitt
xr2, D0r, xl2, D0l, xrM, D0rM, xlM, D0lM = np.genfromtxt('python/stange2.txt', unpack=True)
# in cm, mm, mm
m = 0.605 + 4.6941  # in kg
L = 0.56  # in m, von 0.6 auf 0.56 gesetzt
xr2 *= 1e-2  # x jetzt in m
xrM *= 1e-2
xl2 *= 1e-2
xlM *= 1e-2
a = 10  # Seitenlaenge a in mm
b = 12  # Seitenlaenge b in mm
a *= 1e-3  # a jetzt in m
b *= 1e-3  # b in m
I = (b**3)*a/12  # Flaechentraegheitsmoment für einen quadratischen Querschnitt in m^4
Dr = D0r-D0rM  # Die Ausgleichsrechnung, um die Biegung in Nullage zu beachten
Dl = D0l-D0lM

xr2 *= 1e3
xl2 *= 1e3
xwerter = (3*(L**2)*xr2) - (4*xr2**3)
xwertel = (4*xl2**3) - (12*L*xl2**2) + (9*xl2*L**2) - (L**3)
paramsr, covariance_matrix_r = optimize.curve_fit(f, xwerter, Dr)
paramsl, covariance_matrix_l = optimize.curve_fit(f, xwertel, Dl)
errors_r = np.sqrt(np.diag(covariance_matrix_r))
errors_l = np.sqrt(np.diag(covariance_matrix_l))
print('a_r =', paramsr[0], '+-', errors_r[0])
print('b_r =', paramsr[1], '+-', errors_r[1])
print('a_l =', paramsl[0], '+-', errors_l[0])
print('b_l =', paramsl[1], '+-', errors_l[1])

a_r = ufloat(paramsr[0], errors_r[0])
a_l = ufloat(paramsl[0], errors_l[0])
print(I)
print('E/10^-9 fuer eckig, zweiseitige Einspannung ist (rechts)', (m*9.81)/(48*I*a_r)*1e-9)
print('E/10^-9 fuer eckig, zweiseitige Einspannung ist (links)', (m*9.81)/(48*I*a_l)*1e-9)

plt.plot(xwerter, Dr, 'rx', label='Messwerte')
plt.plot(xwerter, f(xwerter, *paramsr), 'b-', label='fit')
plt.title('Eckiger Stab mit zweiseitiger Einspannung, rechte Seite')
plt.legend()
plt.grid()
plt.xlabel(r'$(3L^2x-4x^3)/$mm³')
plt.ylabel('D(x)/mm')
plt.tight_layout()
plt.savefig('build/quadrat_zweiseitig_rechts.pdf')

plt.clf()

plt.plot(xwertel, Dl, 'rx', label='Messwerte')
plt.plot(xwertel, f(xwertel, *paramsl), 'b-', label='fit')
plt.title('Eckiger Stab mit zweiseitiger Einspannung, linke Seite')
plt.legend()
plt.grid()
plt.xlabel(r'$(4x^3-12Lx^2+9L^2x-L^3)/$mm³')
plt.ylabel('D(x)/mm')
plt.tight_layout()
plt.savefig('build/quadrat_zweiseitig_links.pdf')
plt.clf()
