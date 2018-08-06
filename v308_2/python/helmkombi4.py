import numpy as np
import matplotlib.pyplot as plt

xi, Bi = np.genfromtxt("python/helm4i.txt", unpack=True)
xa, Ba = np.genfromtxt("python/helm4a.txt", unpack=True)

i2 = 4
r = 0.0625
n = 100
xi *= 1e-2
Bi *= 1e-3

plt.plot(xa, Ba, 'k.', label='Messwerte Außen')
plt.plot(xi*1e2, Bi*1e3, 'r--', label='Messwerte Innen')
plt.plot(xi*1e2, 1e3*(((4*np.pi*1e-7*n*i2)/(2*r))*(1/((((xi/r)**2)+(xi/r)+(5/4))**(3/2))
+1/((((xi/r)**2)-(xi/r)+(5/4))**(3/2)))), 'b--', label = 'Theoriewerte')
plt.grid()
plt.xlabel("x / cm")
plt.ylabel("B / mT")
plt.xlim(0.7, 17)
plt.tight_layout(pad=0)
#plt.plot(xa, Ba, "r.", label="Messwerte Außen")
plt.legend()
plt.tight_layout(pad=0)
plt.savefig("build/helmkombi4.pdf", bbox_inches="tight", pad_inches=0)


plt.clf()

plt.plot(xi*1e2, Bi*1e3, 'k--', label='Messwerte Innen')
plt.plot(xi*1e2, 1e3*((4*np.pi*1e-7*n*i2)/(2*r))*(1/((((xi/r)**2)+(xi/r)+(5/4))**(3/2))
+1/((((xi/r)**2)-(xi/r)+(5/4))**(3/2))), 'b--', label = 'Theoriewerte')

plt.legend()
plt.grid()
plt.xlabel("x / cm")
plt.ylabel("B / mT")
plt.tight_layout(pad=0)
plt.savefig("build/4AiZOOM.pdf", bbox_inches="tight", pad_inches=0)
plt.clf()

print('Erwartungswert für Helmholzspulenpaar mit 4A:', (1e3*(4*np.pi*1e-7*n*i2)/(2*r))*(1/((((0/r)**2)+(0/r)+(5/4))**(3/2))
+1/((((0/r)**2)-(0/r)+(5/4))**(3/2))), 'mT')
