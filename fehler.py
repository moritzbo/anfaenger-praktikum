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
r, i = sympy.var('R I_1')
# Formel angeben
u = r * i
print(u)
print(error(u))
print()

# Textdatei, weil ich sonst nicht weiß ob make das kann
r = np.linspace(0,1)
# np.savetxt('build/fehler.txt', (r))
np.savetxt('fehler.txt', r)
