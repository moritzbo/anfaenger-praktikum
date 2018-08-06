import numpy as np
import matplotlib.pyplot as plt

yi, Bi1 = np.genfromtxt("python/helm2i.txt", unpack=True)
ya, Ba1 = np.genfromtxt("python/helm2a.txt", unpack=True)

i1 = 2
r = 0.0625
n = 100

yi *= 1e-2
Bi1 *= 1e-3

plt.plot(ya, Ba1, "r.", label="Messwerte Außen")
plt.plot(yi*1e2, Bi1*1e3, 'r--', label='Messwerte Innen')
plt.plot(yi*1e2, 1e3*((4*np.pi*1e-7*n*i1)/(2*r))*(1/((((yi/r)**2)+(yi/r)+(5/4))**(3/2))
+1/((((yi/r)**2)-(yi/r)+(5/4))**(3/2)))+0*yi, 'b--', label = 'Theoriewerte')
plt.tight_layout()
plt.legend()
plt.grid()
plt.xlabel("x / cm")
plt.ylabel("B / mT")
plt.xlim(0.7, 17)
plt.tight_layout(pad=0)
plt.xlabel("x / cm")
plt.ylabel("B / mT")
plt.tight_layout(pad=0)
plt.savefig("build/helmkombi2.pdf", bbox_inches="tight", pad_inches=0)
plt.clf()

plt.plot(yi*1e2, Bi1*1e3, 'k.', label='Messwerte Innen')
plt.plot(yi*1e2, 1e3*((4*np.pi*1e-7*n*i1)/(2*r))*(1/((((yi/r)**2)+(yi/r)+(5/4))**(3/2))
+1/((((yi/r)**2)-(yi/r)+(5/4))**(3/2)))+0*yi, 'b--', label = 'Theoriewerte')
plt.legend()
plt.grid()
plt.xlabel("x / cm")
plt.ylabel("B / mT")
plt.tight_layout(pad=0)
plt.savefig("build/2AiZOOM.pdf", bbox_inches="tight", pad_inches=0)


plt.clf()
print('Erwartungswert für Helmholzspulenpaar mit 2A:', (1e3*(4*np.pi*1e-7*n*i1)/(2*r))*(1/((((0/r)**2)+(0/r)+(5/4))**(3/2))
+1/((((0/r)**2)-(0/r)+(5/4))**(3/2))), 'mT')
