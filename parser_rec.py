"""
parser_rec.py - Lectura y validación interactiva de la relación de recurrencia.

Formato esperado del usuario:
  Orden k, coeficientes a[0]..a[k-1] tal que:
      a(n) = a[0]*a(n-1) + a[1]*a(n-2) + ... + a[k-1]*a(n-k)

Para el caso heterogéneo también se pide el monomio f(n) = c * n^p.
"""

from sympy import sympify, SympifyError


def leer_coeficientes(orden):
    """Solicita los coeficientes a1, a2, ..., ak de la parte homogénea."""
    coefs = []
    print(f"\n  La relación tiene la forma:")
    partes = " + ".join([f"a{i+1}·a(n-{i+1})" for i in range(orden)])
    print(f"  a(n) = {partes}\n")
    for i in range(orden):
        while True:
            try:
                val = input(f"  Coeficiente a{i+1} (de a(n-{i+1})): ").strip()
                coef = sympify(val)
                coefs.append(coef)
                break
            except (SympifyError, TypeError):
                print("  ✗ Valor no válido. Use números enteros o fracciones (ej: 1/2).")
    return coefs


def leer_condiciones_iniciales(orden):
    """Solicita las condiciones iniciales a(0), a(1), ..., a(k-1)."""
    condiciones = []
    print(f"\n  Ingrese las {orden} condición(es) inicial(es):")
    for i in range(orden):
        while True:
            try:
                val = input(f"  a({i}) = ").strip()
                condiciones.append(sympify(val))
                break
            except (SympifyError, TypeError):
                print("  ✗ Valor no válido.")
    return condiciones


def leer_monomio():
    """Solicita el monomio f(n) = c * n^p con c y p enteros."""
    print("\n  Término no homogéneo f(n) = c · nᵖ")
    while True:
        try:
            c = sympify(input("  Coeficiente c: ").strip())
            break
        except (SympifyError, TypeError):
            print("  ✗ Valor no válido.")
    while True:
        try:
            p = int(input("  Exponente p (entero ≥ 0): ").strip())
            if p >= 0:
                break
            print("  ✗ El exponente debe ser ≥ 0.")
        except ValueError:
            print("  ✗ Ingrese un entero.")
    return c, p


def leer_recurrencia(heterogeneo=False):
    """
    Orquesta la lectura completa.
    Retorna (orden, coefs, condiciones_iniciales) o
            (orden, coefs, condiciones_iniciales, c, p) si heterogéneo.
    Retorna None si el usuario cancela.
    """
    print("\n  (Escriba 'cancelar' en cualquier momento para volver al menú)\n")

    # --- Orden ---
    while True:
        raw = input("  Orden de la recurrencia (k ≥ 1): ").strip()
        if raw.lower() == "cancelar":
            return None
        try:
            orden = int(raw)
            if orden >= 1:
                break
            print("  ✗ El orden debe ser al menos 1.")
        except ValueError:
            print("  ✗ Ingrese un número entero positivo.")

    # --- Coeficientes ---
    coefs = leer_coeficientes(orden)

    # --- Condiciones iniciales ---
    condiciones = leer_condiciones_iniciales(orden)

    if not heterogeneo:
        return orden, coefs, condiciones

    # --- Monomio ---
    c, p = leer_monomio()
    return orden, coefs, condiciones, c, p
