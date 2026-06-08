"""
homogeneo.py - Resuelve relaciones de recurrencia lineales homogéneas
               con coeficientes constantes usando SymPy.

Método:
  1. Construir la ecuación característica.
  2. Factorizar y encontrar raíces (con multiplicidades).
  3. Escribir la solución general (con constantes C1, C2, ...).
  4. Aplicar condiciones iniciales para determinar las constantes.
  5. Mostrar la solución particular y verificar los primeros términos.
"""

from sympy import (
    symbols, Poly, factor_list, solve, Rational, simplify,
    Symbol, pprint, Eq, linsolve, Matrix, factorial
)
from sympy import Integer as SInt


def ecuacion_caracteristica(coefs):
    """
    Dado [a1, a2, ..., ak], construye el polinomio característico:
        r^k - a1·r^(k-1) - a2·r^(k-2) - ... - ak = 0
    Retorna (r, poly_expr).
    """
    r = symbols('r')
    k = len(coefs)
    poly = r**k
    for i, a in enumerate(coefs):
        poly -= a * r**(k - 1 - i)
    return r, poly


def obtener_raices(r, poly):
    """
    Calcula raíces con multiplicidades.
    Retorna lista de (raíz, multiplicidad).
    """
    raices_raw = solve(poly, r)
    # Usar Poly para obtener multiplicidades exactas
    p = Poly(poly, r)
    factores = factor_list(poly, r)  # (coef, [(factor, mult), ...])
    
    raices = []
    for factor, mult in factores[1]:
        sols = solve(factor, r)
        for s in sols:
            raices.append((s, mult))
    
    # Si factor_list no funcionó bien, caer en solve sin multiplicidades
    if not raices:
        for s in raices_raw:
            raices.append((s, 1))
    
    return raices


def construir_solucion_general(raices, n):
    """
    Construye la solución general simbólica.
    Para cada raíz r con multiplicidad m:
        (C_i + C_{i+1}·n + ... + C_{i+m-1}·n^{m-1}) · r^n
    Retorna (expresión, lista_de_constantes).
    """
    terminos = []
    constantes = []
    idx = 1
    for raiz, mult in raices:
        for j in range(mult):
            C = symbols(f'C{idx}')
            constantes.append(C)
            terminos.append(C * n**j * raiz**n)
            idx += 1
    sol_general = sum(terminos)
    return sol_general, constantes


def aplicar_condiciones(sol_general, constantes, condiciones, n):
    """
    Sustituye n = 0, 1, ..., k-1 para formar un sistema lineal
    y resuelve para C1, ..., Ck.
    Retorna el diccionario {Ci: valor}.
    """
    ecuaciones = []
    for i, val in enumerate(condiciones):
        eq = Eq(sol_general.subs(n, i), val)
        ecuaciones.append(eq)

    solucion = linsolve(ecuaciones, constantes)
    if not solucion:
        # Intentar con solve normal
        solucion_dict = {}
        sols = solve(ecuaciones, constantes)
        if isinstance(sols, dict):
            solucion_dict = sols
        return solucion_dict

    sol_list = list(solucion)[0]
    return {c: v for c, v in zip(constantes, sol_list)}


def calcular_terminos(sol_particular, n, cantidad=8):
    """Evalúa los primeros 'cantidad' términos de la solución."""
    terminos = []
    for i in range(cantidad):
        val = simplify(sol_particular.subs(n, i))
        terminos.append(val)
    return terminos


def mostrar_resultado(orden, coefs, condiciones, raices, sol_general,
                      constantes, valores_C, sol_particular, n):
    """Imprime el proceso completo de resolución."""
    sep = "─" * 60

    print(f"\n{sep}")
    print("  SOLUCIÓN — CASO HOMOGÉNEO")
    print(sep)

    # Relación de recurrencia
    partes = " + ".join([f"({coefs[i]})·a(n-{i+1})" for i in range(orden)])
    print(f"\n  Relación:  a(n) = {partes}")
    cond_str = ",  ".join([f"a({i})={v}" for i, v in enumerate(condiciones)])
    print(f"  C. iniciales: {cond_str}")

    # Ecuación característica
    r = symbols('r')
    poly_str = " - ".join(
        [f"r^{orden}"] + [f"({coefs[i]})·r^{orden-1-i}" for i in range(orden)]
    )
    print(f"\n  Ec. característica: {poly_str} = 0")

    # Raíces
    print("\n  Raíces características:")
    for raiz, mult in raices:
        if mult == 1:
            print(f"    r = {raiz}")
        else:
            print(f"    r = {raiz}  (multiplicidad {mult})")

    # Solución general
    print("\n  Solución general:")
    print("    a(n) = ", end="")
    pprint(sol_general, use_unicode=True)

    # Valores de constantes
    print("\n  Constantes (por condiciones iniciales):")
    for c, v in valores_C.items():
        print(f"    {c} = {v}")

    # Solución particular
    sol_simp = simplify(sol_particular)
    print("\n  Solución particular:")
    print("    a(n) = ", end="")
    pprint(sol_simp, use_unicode=True)

    # Verificación
    terminos = calcular_terminos(sol_particular, n)
    print("\n  Primeros términos:")
    vals = "  ".join([f"a({i})={v}" for i, v in enumerate(terminos)])
    print(f"    {vals}")
    print(f"\n{sep}\n")


def resolver_homogeneo(orden, coefs, condiciones):
    """Función principal: orquesta la resolución homogénea."""
    n = symbols('n')

    r, poly = ecuacion_caracteristica(coefs)
    raices = obtener_raices(r, poly)
    sol_general, constantes = construir_solucion_general(raices, n)
    valores_C = aplicar_condiciones(sol_general, constantes, condiciones, n)
    sol_particular = sol_general.subs(valores_C)

    mostrar_resultado(orden, coefs, condiciones, raices, sol_general,
                      constantes, valores_C, sol_particular, n)
