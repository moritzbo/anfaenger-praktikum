import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy import optimize
import scipy.constants as const
from scipy.stats import sem
import unittest

Tc = [26.1, 153]  # beide temperaturen in celsius
Tk = [299.25, 426.15]  # beide temperaturen in kelvin
print("-------------sättigungsdruck----------")

psät1 = 5.5e7*np.exp(-(6876/Tk[0]))  # in mbar
psät2 = 5.5e7*np.exp(-(6876/Tk[1]))
n = 0
for n in Tk:
    print("psät=", 5.5e7*np.exp(-(6876/n)), "mbar")
    n = n+1

print("-------w_quer---------")

w1 = (0.0029)/(psät1)
w2 = (0.0029)/(psät2)

print("w1 =", w1, "cm")
print("w2 =", w2, "cm")
