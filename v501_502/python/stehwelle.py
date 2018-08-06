import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
from scipy.stats import sem
N, f = np.genfromtxt("python/stehwelle.txt", unpack=True)


# N[-1] = 14
# def fit(x, a, b):
#     return a * x + b
# params, covariance_matrix = optimize.curve_fit(fit, N, f)
# errors = np.sqrt(np.diag(covariance_matrix))
# print('a =', params[0],'+/-', errors[0])
# print('b =', params[1],'+/-', errors[1])
# m = np.linspace(1,14)
# plt.plot(m, params[0]*m+params[1], linewidth=0.1)
# plt.plot(N, f, linewidth=0.1)
# plt.xlim(1, 14)
# plt.ylim(29, 160)
# plt.savefig('build/stehwelle.pdf')
sae12 = f[1]
sae1 = f[5]
sae2 = f[6]
sae = np.array([sae12,sae1,sae2])
sin = np.array([sae12*2,sae1,sae2/2])
print('mean', np.mean(sin))
print('sem', sem(sin))
np.savetxt('build/stehwelle.txt', np.column_stack([sae,sin]), header='sae, sin')
