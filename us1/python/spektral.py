import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
import uncertainties.unumpy as unp
from scipy import optimize
import scipy.constants as const
from scipy.stats import sem

v, amp = np.genfromtxt('python/fftwerte.txt', unpack=True)
# print(len(v), len(amp))
plt.plot(v, amp, "b--", label="fft")
plt.grid()
plt.xlabel("f / MHz")
plt.ylabel("A / mV")
plt.legend()
plt.savefig("build/fft.pdf")

plt.clf()
