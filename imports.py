
import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
import uncertainties.unumpy as unp
from scipy import optimize
import scipy.constants as const
from scipy.stats import sem

np.genfromtxt('python/*.txt', unpack=True)

np.savetxt('build/*.txt', np.column_stack([*, *]), header='*')

params, covariance_matrix = optimize.curve_fit(function, array1, array2)
errors = np.sqrt(np.diag(covariance_matrix))
param0 = ufloat(params[0], errors[0])
