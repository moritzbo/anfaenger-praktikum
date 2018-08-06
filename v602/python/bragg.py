import numpy as np
import matplotlib.pyplot as plt

theta, impuls = np.genfromtxt('python/bragg.txt', unpack=True)

print('28-27.6=0.4')
print('100*(28-27.6)/28=',100*(28-27.6)/28)

plt.plot(theta, impuls, 'bx')
plt.plot([28, 28], [0, 300], 'r-', label='Theoriewert')
plt.xlabel(r'$φ\;/\;\si{\degree}$')
plt.ylabel('Counts')
plt.xlim(25.8, 30.2)
plt.ylim(35, 300)
plt.grid()
plt.tight_layout()
plt.savefig('build/bragg.pdf')
