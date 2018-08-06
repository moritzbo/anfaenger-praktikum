import numpy as np
import matplotlib.pyplot as plt

mu = 4*np.pi*1e-7
I1 = 1  # strom kurze spule in ampere
n1 = 100  # kurze spule
l1 = 0.055  # länge in meter

I2 = 1  # strom durch lange spule in A
n2 = 300  # lange spule
l2 = 0.16  # länge in meter
R2 = 0.047  # radius in meter

#  lange Spule
xl, Bl = np.genfromtxt("python/spuleL.txt", unpack=True)
xl *= 1e-2  # x in meter
Bl *= 1e-3  # B in Tesla

x = np.linspace(0, 0.27)

plt.plot(xl*1e2, Bl*1e3, "b-", label="Messwerte")
plt.plot(x*1e2, 1e3*(4*np.pi*1e-7*n2/(0.16)*I2/(2))*((x-0.05)/(np.sqrt(((x-0.05)**2)+((R2/2)**2)))
-(x-0.23)/(np.sqrt(((x-0.23)**2)+((R2/2)**2)))), "g--", label="Theoriewerte")
plt.legend()
plt.grid()
plt.xlabel("x / cm")
plt.ylabel("B / mT")
plt.tight_layout(pad=0)
plt.savefig("build/spulen.pdf", bbox_inches="tight", pad_inches=0)
#  ENDE kurze Spule

plt.clf()

#  kurze Spule
xk, Bk = np.genfromtxt("python/spuleK.txt", unpack=True)
Bk *= 1e-3
xk *= 1e-2
y1 = 1e3*(4*np.pi*1e-7*n1/(0.055)*I1/(2))*((x-0.06)/(np.sqrt(((x-0.06)**2)+((R2/(2))**2)))
-(x-0.115)/(np.sqrt(((x-0.115)**2)+((R2/(2))**2))))

y = np.linspace(0, 0.17)

plt.plot(xk*1e2, Bk*1e3, "g-", label="Messwerte")
plt.plot(y*1e2, y1, "g--", label="Theoriewerte")
plt.legend()
plt.grid()
plt.xlabel("x / cm")
plt.ylabel("B / mT")
plt.tight_layout(pad=0)
plt.savefig("build/spule_kurz.pdf", bbox_inches="tight", pad_inches=0)
#  ENDE kurze Spule

#  maxwert der kurzen Spule
Y1 = 1e3*(4*np.pi*1e-7*n1/(0.055)*I1/(2))*((0.095-0.06)/(np.sqrt(((0.095-0.06)**2)+((R2/(2))**2)))
-(0.095-0.115)/(np.sqrt(((0.095-0.115)**2)+((R2/(2))**2))))

#  maxwert der langen Spule
Y2 = 1e3*(4*np.pi*1e-7*n2/(0.16)*I2/(2))*((0.17-0.05)/(np.sqrt(((0.17-0.05)**2)+((R2/2)**2)))
-(0.17-0.23)/(np.sqrt(((0.17-0.23)**2)+((R2/2)**2))))
plt.clf()

print("Der Erwartungswert der langen Spule:", Y2)
print("Der Erwartungswert der kurzen Spule:", Y1)
