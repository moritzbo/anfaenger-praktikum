import sympy
import numpy as np


def error(f, err_vars=None):
    from sympy import Symbol, latex
    s = 0
    latex_names = dict()

    if err_vars is None:
        err_vars = f.free_symbols

    for v in err_vars:
        err = Symbol('latex_std_' + v.name)
        s += f.diff(v)**2 * err**2
        latex_names[err] = '\\sigma_{' + latex(v) + '}'

    return latex(sympy.sqrt(s), symbol_names=latex_names)


pot, r2 = sympy.var('\frac{R_3}{R_4} R_2')
r = r2 * pot
print(r)
print(error(r))
print()

pot, c2 = sympy.var('\frac{R_3}{R_4} C_2')
c = c2 / pot
print(c)
print(error(c))
print()

pot, l2 = sympy.var('\frac{R_3}{R_4} L_2')
l = l2 * pot
print(l)
print(error(l))
print()

r2, r3, c4 = sympy.var('R_2 R_3 C_4')
lm = r2 * r3 * c4
print(lm)
print(error(lm))
print()

l1, l2, l3 = sympy.var('L_1 L_2 L_3')
m = l1 + l2 + l3
print(m)
print(error(m))

x = np.linspace(0, 1)
np.savetxt('build/fehler.txt', x)
