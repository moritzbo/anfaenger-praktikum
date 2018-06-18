import numpy as np
import matplotlib.pyplot as plt

n, t1, t2, t3, t4, t5, t6, t7, t8 = np.genfromtxt('python/statisch.txt', unpack=True)
plt.plot(5*n-5, t1, 'bo', markersize=1, label=r'$T_1$,\;Messing (breit)')
plt.plot(5*n-5, t4, 'ro', markersize=1, label=r'$T_4$,\;Messing (schmal)')
plt.plot(5*n-5, t5, 'ko', markersize=1, label=r'$T_5$,\;Aluminium')
plt.plot(5*n-5, t8, 'yo', markersize=1, label=r'$T_8$,\;Edelstahl')
plt.legend()
plt.grid()
plt.xlabel(r'$t\:/\:\si{\second}$')
plt.ylabel(r'$T\:/\:\si{\celsius}$')
plt.xlim(0, 960)
plt.ylim(15, 51)
plt.tight_layout(pad=0)
plt.savefig('build/statisch.pdf', bbox_inches='tight', pad_inches=0)
plt.clf()
print('t=700')
print('T1', t1[139])
print('T4', t4[139])
print('T5', t5[139])
print('T8', t8[139])

plt.plot(5*n, t7-t8, 'yx', markersize=3, label=r'$T_7-T_8$')
plt.plot(5*n, t2-t1, 'bx', markersize=3, label=r'$T_2-T_1$')
plt.legend(loc='lower right')
plt.grid()
plt.xlabel(r'$t\:/\:\si{\second}$')
plt.ylabel(r'$\symup{Δ}T\:/\:\si{\celsius}$')
plt.xlim(0, 960)
plt.ylim(-2, 12)
plt.tight_layout(pad=0)
plt.savefig('build/statisch-unterschied.pdf', bbox_inches='tight', pad_inches=0)
plt.clf()

np.savetxt('build/statisch.txt', np.column_stack([5*n, t1, t2, t2-t1, t4, t5, t7, t8, t7-t8]), header='t, T1, T2, T2-T1, T4, T5, T7, T8, T7-T8')

As = 0.004 * 0.007
Ab = 0.004 * 0.012
deltax = 0.03
zeiten = np.array([20, 60, 100, 140, 180])
messingschmall = -90*As*(t3[zeiten]-t4[zeiten])/deltax
messingbreit = -90*Ab*(t2[zeiten]-t1[zeiten])/deltax
aluminium = -220*Ab*(t6[zeiten]-t5[zeiten])/deltax
edelstahl = -21*Ab*(t7[zeiten]-t8[zeiten])/deltax
np.savetxt('build/waermestrom.txt', np.column_stack([5*zeiten, messingschmall, messingbreit, aluminium, edelstahl]), header='zeiten, messingschmall, messingbreit, aluminium, edelstahl')
print('aschmall', As)
print('abreit', Ab)
print('messingschmall/7, messingbreit/12')
print(np.column_stack([messingschmall/7, messingbreit/12]))
