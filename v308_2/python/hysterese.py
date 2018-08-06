import numpy as np
import matplotlib.pyplot as plt

I, B = np.genfromtxt("python/hysterese.txt", unpack=True)

plt.plot(I, B, "b--", label="Messwerte")
#  Geraden der Koerzitivfeldstärke
m1 = B[20]-B[22]
b1 = B[20]
m2 = B[43]-B[41]
b2 = B[41]
x = np.linspace(-2.5, 2.5)
f1 = m1*x + b1
f2 = m2*x + b2
plt.plot(x, f1, "r-", label="Gerade 1")
plt.plot(x, f2, "r-", label="Gerade 2")

plt.legend()
plt.grid()
plt.xlabel("I / A")
plt.ylabel("B / mT")
plt.tight_layout(pad=0)
plt.savefig("build/hysterese.pdf", bbox_inches="tight", pad_inches=0)

plt.clf()
