"""
heterogeneo.py - Resuelve relaciones de recurrencia lineales NO homogéneas
                 cuando el término adicional es un monomio f(n) = c · n^p.

Método (variación de parámetros / solución particular por forma supuesta):
  - La solución general es:  a(n) = a_h(n) + a_p(n)
  - a_h(n): solución de la parte homogénea asociada.
  - a_p(n): solución particular, cuya forma se elige según f(n) = c·n^p:
      * Si r=1 NO es raíz característica:
            a_p(n) = d_0 + d_1·n + ... + d_p·n^p
      * Si r=1 es raíz de multiplicidad m:
            a_p(n) = n^m · (d_0 + d_1·n + ... + d_p·n^p)

  Los coeficientes d_i se determinan sustituyendo a_p en la recurrencia.
"""

from sympy import (
    symbols, Poly, factor_list, solve, simplify, linsolve,
    Eq, pprint, Symbol, Rational, expand
)
from homogeneo import (
    ecuacion_caracteristica, obtener_raices,
    construir_solucion_general, aplicar_condiciones, calcular_terminos
)


def multiplicidad_raiz_uno(raices):
    """Retorna la multiplicidad de r=1 en la lista de raíces, o 0 si no está."""
    for raiz, mult in raices:
        if simplify(raiz - 1) == 0:
            return mult
    return 0


def forma_solucion_particular(p, mult_uno):
    """
    Construye la forma supuesta de a_p(n).
    d0, d1, ..., dp son los coeficientes a determinar.
    Retorna (a_p_expr, [d0, d1, ..., dp]).
    """
    n = symbols('n')
    d_syms = [symbols(f'd{i}') for i in range(p + 1)]
    polinomio = sum(d_syms[i] * n**i for i in range(p + 1))
    a_p = n**mult_uno * polinomio
    return a_p, d_syms


def determinar_coeficientes_particulares(a_p, d_syms, coefs, c, p):
    """
    Sustituye a_p(n) en la recurrencia:
        a_p(n) - sum(a_i * a_p(n-i)) = c·n^p
    Iguala coeficientes del polinomio resultante para hallar d_i.
    """
    n = symbols('n')
    k = len(coefs)

    # Lado izquierdo: a_p(n) - a1·a_p(n-1) - ... - ak·a_p(n-k)
    lhs = expand(a_p)
    for i, a in enumerate(coefs):
        lhs -= a * expand(a_p.subs(n, n - (i + 1)))

    # Lado derecho: c·n^p
    rhs = c * n**p

    # Diferencia: lhs - rhs = 0, expandir y recoger por potencias de n
    diferencia = expand(lhs - rhs)

    # Obtener coeficientes del polinomio en n
    poly_diff = Poly(diferencia, n)
    coef_dict = poly_diff.as_dict()

    # Ecuaciones: cada coeficiente de n^i debe ser 0
    ecuaciones = [simplify(v) for v in coef_dict.values()]

    solucion = solve(ecuaciones, d_syms)
    return solucion


def resolver_heterogeneo(orden, coefs, condiciones, c, p):
    """Función principal: orquesta la resolución heterogénea."""
    n = symbols('n')
    sep = "─" * 60

    # 1. Parte homogénea
    r, poly = ecuacion_caracteristica(coefs)
    raices = obtener_raices(r, poly)
    sol_h, constantes = construir_solucion_general(raices, n)

    # 2. Multiplicidad de r=1
    mult_uno = multiplicidad_raiz_uno(raices)

    # 3. Forma de la solución particular
    a_p, d_syms = forma_solucion_particular(p, mult_uno)

    # 4. Determinar coeficientes particulares
    valores_d = determinar_coeficientes_particulares(a_p, d_syms, coefs, c, p)

    if not valores_d:
        print("\n  ✗ No se pudo determinar la solución particular automáticamente.")
        print("    Verifique que el monomio esté bien definido.")
        return

    a_p_particular = a_p.subs(valores_d)

    # 5. Solución general completa
    sol_completa = sol_h + a_p_particular

    # 6. Aplicar condiciones iniciales
    valores_C = aplicar_condiciones(sol_completa, constantes, condiciones, n)
    sol_final = sol_completa.subs(valores_C)

    # --- Presentación ---
    print(f"\n{sep}")
    print("  SOLUCIÓN — CASO HETEROGÉNEO (término monomio)")
    print(sep)

    partes = " + ".join([f"({coefs[i]})·a(n-{i+1})" for i in range(orden)])
    fn = f"({c})·n^{p}" if p > 0 else f"({c})"
    print(f"\n  Relación:  a(n) = {partes}  +  {fn}")
    cond_str = ",  ".join([f"a({i})={v}" for i, v in enumerate(condiciones)])
    print(f"  C. iniciales: {cond_str}")

    print(f"\n  Raíces características:")
    for raiz, mult in raices:
        tag = f"  (mult. {mult})" if mult > 1 else ""
        print(f"    r = {raiz}{tag}")

    print(f"\n  Multiplicidad de r=1: {mult_uno}")
    print(f"  Forma supuesta de a_p(n):")
    print("    a_p(n) = ", end="")
    pprint(a_p, use_unicode=True)

    print(f"\n  Coeficientes particulares: {valores_d}")

    print(f"\n  Solución particular:")
    print("    a_p(n) = ", end="")
    pprint(simplify(a_p_particular), use_unicode=True)

    print(f"\n  Solución homogénea general:")
    print("    a_h(n) = ", end="")
    pprint(sol_h, use_unicode=True)

    print(f"\n  Constantes (por condiciones iniciales): {valores_C}")

    sol_simp = simplify(sol_final)
    print(f"\n  Solución completa:")
    print("    a(n) = ", end="")
    pprint(sol_simp, use_unicode=True)

    terminos = calcular_terminos(sol_final, n, cantidad=8)
    print("\n  Primeros términos:")
    vals = "  ".join([f"a({i})={v}" for i, v in enumerate(terminos)])
    print(f"    {vals}")
    print(f"\n{sep}\n")
