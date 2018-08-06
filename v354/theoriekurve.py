import numpy as np
import matplotlib.pyplot as plt


def f(v, r, c, l):
    return (1 / np.sqrt((1 - v**2 * l * c)**2 + (v**2 * r**2 * c**2)))


def phi(v, r, c, l):
    return np.arctan((-v * r * c)/(1 - l * c * v**2))


x = np.linspace(0, 60000, 20)
m = 559.5
n = 2.098*10**(-9)
b = 10.11*10**(-3)
# y = f(x, r, c, l)
print(m, n, b)
print(    0, f(    0*2*np.pi, m, n, b))
print( 5000, f( 5000*2*np.pi, m, n, b))
print(10000, f(10000*2*np.pi, m, n, b))
print(15000, f(15000*2*np.pi, m, n, b))
print(20000, f(20000*2*np.pi, m, n, b))
print(25000, f(25000*2*np.pi, m, n, b))
print(30000, f(30000*2*np.pi, m, n, b))
print(35000, f(35000*2*np.pi, m, n, b))
print(40000, f(40000*2*np.pi, m, n, b))
print(45000, f(45000*2*np.pi, m, n, b))
print(50000, f(50000*2*np.pi, m, n, b))
print(55000, f(55000*2*np.pi, m, n, b))
print(60000, f(60000*2*np.pi, m, n, b))

print('sdfh')
print(    0, -180 / np.pi * phi(    0*2*np.pi, m, n, b))
print( 5000, -180 / np.pi * phi( 5000*2*np.pi, m, n, b))
print(10000, -180 / np.pi * phi(10000*2*np.pi, m, n, b))
print(15000, -180 / np.pi * phi(15000*2*np.pi, m, n, b))
print(20000, -180 / np.pi * phi(20000*2*np.pi, m, n, b))
print(25000, -180 / np.pi * phi(25000*2*np.pi, m, n, b))
print(30000, -180 / np.pi * phi(30000*2*np.pi, m, n, b))
print(31000, -180 / np.pi * phi(31000*2*np.pi, m, n, b))
print(32000, -180 / np.pi * phi(32000*2*np.pi, m, n, b))
print(33000, -180 / np.pi * phi(33000*2*np.pi, m, n, b))
print(34000, -180 / np.pi * (phi(34000*2*np.pi, m, n, b)))
print(35000, -180 / np.pi * (phi(35000*2*np.pi, m, n, b) - np.pi))
print(36000, -180 / np.pi * (phi(36000*2*np.pi, m, n, b) - np.pi))
print(37000, -180 / np.pi * (phi(37000*2*np.pi, m, n, b) - np.pi))
print(38000, -180 / np.pi * (phi(38000*2*np.pi, m, n, b) - np.pi))
print(39000, -180 / np.pi * (phi(39000*2*np.pi, m, n, b) - np.pi))
print(40000, -180 / np.pi * (phi(40000*2*np.pi, m, n, b) - np.pi))
print(45000, -180 / np.pi * (phi(45000*2*np.pi, m, n, b) - np.pi))
print(50000, -180 / np.pi * (phi(50000*2*np.pi, m, n, b) - np.pi))

# plt.plot(x, y, 'b-')
# plt.grid()
# plt.yscale('log')
# plt.show()
# plt.clf()
