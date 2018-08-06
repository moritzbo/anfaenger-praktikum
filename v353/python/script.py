import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
from uncertainties import ufloat

print('Entladung ANFANG')


def f(x, a, b):
    return a*x+b


t, U = np.genfromtxt('python/daten/werte_a.txt', unpack=True)  # unsere Messwerte
#  in ms, Volt
t *= 1e-3  # jetzt in s
m = np.linspace(0, 0.3, 20)
lnU = np.log(U/U[0])  # Logarithmus der reduzierten Spannungen
params, covariance_matrix = optimize.curve_fit(f, t, lnU)
errors = np.sqrt(np.diag(covariance_matrix))

a = ufloat(params[0], errors[0])
print('Entladung, RC =', -1/a)

plt.plot(t, lnU, 'k.', label='Messwerte')  # werte gegeneinander aufgetragen
plt.plot(m, f(m, params[0], params[1]), 'g-', label='Ausgleichsgerade')
plt.legend()
plt.grid()
plt.xlim(0, 0.205)
plt.ylim(-2.7, 0)
plt.xlabel("t / s")
plt.ylabel(r'$\log\left(\frac{U_\text{C}}{U_0}\right)$')
# plt.show()
plt.tight_layout(pad=0)
plt.savefig('build/linreg_a.pdf', bbox_inches='tight', pad_inches=0)
np.savetxt('build/werte_a.txt', np.column_stack([t, U, lnU]), header="Zeit/s U_C/V ln(U_C/U(0))")
# linreg für Bestimmung von RC fertig
plt.clf()

print('Entladung ENDE')


f, U0, Uc, dt = np.genfromtxt('python/daten/werte_b_c.txt', unpack=True)

print('Phasenplot ANFANG')


# Phasenplot
def phase(x, a):
    return np.arctan(2*np.pi * a*x)/(np.pi)/2 * 360


dt *= 1e6  # von micro- auf sekunden
phi = (dt*f*360)/1e12  # mit f = 1/T

params, covariance_matrix = optimize.curve_fit(phase, f, phi)
errors = np.sqrt(np.diag(covariance_matrix))

RC = ufloat(params[0], errors[0])
nrc = params[0]
freq = np.linspace(0, 6000, 5000)
print('Phasenplot, RC = ', RC)
plt.plot(f, phi, 'rx', label='Messwerte')
plt.plot(freq, phase(freq, params[0]), 'k-', label='Fitfunktion')
plt.xscale('log')
plt.xlim(8, 6000)
plt.ylim(0, 90)
plt.xlabel('f / Hz')
plt.ylabel('$φ$ / °')
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig('build/phasenplot.pdf')
np.savetxt('build/phase.txt', np.column_stack([f, U0, Uc, dt, phi]), header="f, U0, Uc, dt, phi")

# Phasenplot Ende
plt.clf()

print('Phasenplot ENDE')

print('Amplitudenplot ANFANG')
# Amplitudenplot
u = Uc/Uc[0]


def amplitude(x, a):
    return 1/np.sqrt(1+4*(np.pi**2)*(x**2)*(a**2))


params, covariance_matrix = optimize.curve_fit(amplitude, f, u)
errors = np.sqrt(np.diag(covariance_matrix))
rc = ufloat(params[0], errors[0])
print('Amplitudenplot, RC = ', rc)
plt.plot(f, u, 'rx', label='Messwerte')
plt.plot(freq, amplitude(freq, params[0]), 'k-', label='Fitfunktion')
plt.xscale('log')
plt.xlim(8, 6000)
plt.ylim(0, 1.05)
plt.xlabel('f / Hz')
plt.ylabel(r'$\frac{U_\text{C}}{U_\text{C}{(0)}}')
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig('build/amplitudenplot.pdf')
np.savetxt('build/amplitude.txt', np.column_stack([f, U0, Uc, u]), header="f, U0, Uc, u")
# Amplitudenplot Ende
plt.clf()

print('Amplitudenplot ENDE')

print('Polarplot ANFANG')
# Polarplot
w = f*2*np.pi
w2 = freq*2*np.pi + 1e-20
phi = phi * np.pi / 180
phi2 = np.arctan(w2*nrc)
a = np.sin(phi2)/(w2*nrc)

fig1 = plt.figure()
ax1 = fig1.add_axes([0.1, 0.1, 0.8, 0.8], polar=True)
ax1.set_ylim(0, 1.2)
ax1.set_yticks([1, 1.2], [1, 1.2])
ax1.plot(phi, u, 'rx', label='Messwerte')
ax1.plot(phi2, a, 'b-', label='Theoriewerte')
ax1.legend(loc='lower left')
plt.savefig('build/polarplot.pdf')
np.savetxt('build/polar.txt', np.column_stack([f, w, phi, u]), header='f, w, phi, u')
# Polarplot Ende
plt.clf()

print('Polarplot ENDE')

print('Python Ende')
