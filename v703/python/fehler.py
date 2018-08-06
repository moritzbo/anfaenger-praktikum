import sympy
import numpy as np


def error(f, err_vars=None):
    from sympy import Symbol, latex
    s = 0
    latex_names = dict()

    if err_vars == None:
        err_vars = f.free_symbols

    for v in err_vars:
        err = Symbol('latex_std_' + v.name)
        s += f.diff(v)**2 * err**2
        latex_names[err] = '\\sigma_{' + latex(v) + '}'

    return latex(sympy.sqrt(s), symbol_names=latex_names)

# fehlerbehaftete Variablen mit , getrennt definieren, in Klammern den Tex-Namen schreiben
a, b = sympy.var('N_a N_b')
# Formel angeben
u = (b-a)/(b)*100
print(u)
print(error(u))
print()

n1, n12, n2 = sympy.var('N_1 N_{1+2} N_2')
u = (n1 - n12 + n2)/(2 * n1 * n2)
print(u)
print(error(u))
print()

i, dt, n = sympy.var('bar{I} \increment N_{\SI{1}{\second}}')
q = i*dt/n
print(q)
print(error(q))
print()

# Textdatei, weil ich sonst nicht weiß ob make das kann
r = np.linspace(0,1,1)
# np.savetxt('build/fehler.txt', (r))
np.savetxt('build/zzz.txt', r)
