from sympy import symbols, solve, simplify

def resolver_hlcc2(a, b, f0, f1):

    x = symbols('x')

    polinomio = x**2 - a*x - b

    raices = solve(polinomio, x)

    n = symbols('n')

    if len(set(raices)) == 2:

        r1, r2 = raices

        beta = simplify((f1 - f0*r1)/(r2 - r1))
        alpha = simplify(f0 - beta)

        solucion = simplify(alpha*r1**n + beta*r2**n)

        return {
            "tipo": "distintas",
            "raices": (r1, r2),
            "alpha": alpha,
            "beta": beta,
            "solucion": solucion
        }

    else:

        r = raices[0]

        alpha = f0
        beta = simplify((f1 - f0*r)/r)

        solucion = simplify(alpha*r**n + beta*n*r**n)

        return {
            "tipo": "repetida",
            "raices": (r,),
            "alpha": alpha,
            "beta": beta,
            "solucion": solucion
        }