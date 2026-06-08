"""
ejemplos.py - Ejemplos predefinidos de relaciones de recurrencia.

Incluye casos homogéneos y heterogéneos variados para demostración.
"""

from homogeneo import resolver_homogeneo
from heterogeneo import resolver_heterogeneo


EJEMPLOS = [
    # ── HOMOGÉNEOS ──────────────────────────────────────────────────────────
    {
        "titulo": "EJ-H1: Fibonacci  →  a(n) = a(n-1) + a(n-2)",
        "tipo": "homogeneo",
        "descripcion": (
            "La célebre sucesión de Fibonacci. Raíces: φ = (1+√5)/2 y ψ = (1-√5)/2.\n"
            "  Fórmula de Binet: a(n) = (φⁿ - ψⁿ)/√5"
        ),
        "orden": 2,
        "coefs": [1, 1],
        "condiciones": [0, 1],
    },
    {
        "titulo": "EJ-H2: Raíz doble  →  a(n) = 4a(n-1) - 4a(n-2)",
        "tipo": "homogeneo",
        "descripcion": (
            "Ec. característica: (r-2)² = 0  →  raíz doble r=2.\n"
            "  Solución general: a(n) = (C1 + C2·n)·2ⁿ"
        ),
        "orden": 2,
        "coefs": [4, -4],
        "condiciones": [1, 4],
    },
    {
        "titulo": "EJ-H3: Orden 3  →  a(n) = 6a(n-1) - 11a(n-2) + 6a(n-3)",
        "tipo": "homogeneo",
        "descripcion": (
            "Ec. característica: (r-1)(r-2)(r-3) = 0  →  raíces 1, 2, 3.\n"
            "  Solución general: a(n) = C1 + C2·2ⁿ + C3·3ⁿ"
        ),
        "orden": 3,
        "coefs": [6, -11, 6],
        "condiciones": [0, 1, 3],
    },
    {
        "titulo": "EJ-H4: Crecimiento simple  →  a(n) = 3a(n-1)",
        "tipo": "homogeneo",
        "descripcion": (
            "Orden 1. Raíz característica r=3.\n"
            "  Solución: a(n) = a(0)·3ⁿ"
        ),
        "orden": 1,
        "coefs": [3],
        "condiciones": [2],
    },
    # ── HETEROGÉNEOS ────────────────────────────────────────────────────────
    {
        "titulo": "EJ-X1: a(n) = 2a(n-1) + n   [r=1 no es raíz]",
        "tipo": "heterogeneo",
        "descripcion": (
            "Parte homogénea: a_h(n) = C1·2ⁿ.\n"
            "r=1 no es raíz  →  a_p(n) = d0 + d1·n  (polinomio de grado 1)."
        ),
        "orden": 1,
        "coefs": [2],
        "condiciones": [0],
        "c": 1,
        "p": 1,
    },
    {
        "titulo": "EJ-X2: a(n) = a(n-1) + n²   [r=1 es raíz simple]",
        "tipo": "heterogeneo",
        "descripcion": (
            "Parte homogénea: a_h(n) = C1·1ⁿ = C1.\n"
            "r=1 es raíz simple (m=1)  →  a_p(n) = n·(d0 + d1·n + d2·n²)."
        ),
        "orden": 1,
        "coefs": [1],
        "condiciones": [0],
        "c": 1,
        "p": 2,
    },
    {
        "titulo": "EJ-X3: a(n) = 5a(n-1) - 6a(n-2) + 4   [monomio constante]",
        "tipo": "heterogeneo",
        "descripcion": (
            "Raíces 2 y 3. r=1 no es raíz  →  a_p(n) = d0 (constante).\n"
            "f(n) = 4 = 4·n⁰."
        ),
        "orden": 2,
        "coefs": [5, -6],
        "condiciones": [1, 2],
        "c": 4,
        "p": 0,
    },
    {
        "titulo": "EJ-X4: a(n) = 2a(n-1) - a(n-2) + 3n   [r=1 raíz doble]",
        "tipo": "heterogeneo",
        "descripcion": (
            "Ec. característica: (r-1)² = 0  →  raíz doble r=1 (m=2).\n"
            "a_p(n) = n²·(d0 + d1·n)  por la multiplicidad."
        ),
        "orden": 2,
        "coefs": [2, -1],
        "condiciones": [0, 0],
        "c": 3,
        "p": 1,
    },
]


def ejecutar_ejemplos():
    """Presenta el menú de ejemplos y ejecuta el seleccionado."""
    sep = "═" * 60
    print(f"\n{sep}")
    print("  EJEMPLOS PREDEFINIDOS")
    print(sep)

    for i, ej in enumerate(EJEMPLOS, 1):
        tipo_tag = "[H]" if ej["tipo"] == "homogeneo" else "[X]"
        print(f"  {i}. {tipo_tag} {ej['titulo']}")

    print(f"  {len(EJEMPLOS)+1}. Ejecutar TODOS los ejemplos")
    print(f"  0. Volver al menú principal")

    while True:
        raw = input("\n  Seleccione un ejemplo: ").strip()
        try:
            opcion = int(raw)
        except ValueError:
            print("  ✗ Ingrese un número.")
            continue

        if opcion == 0:
            return
        elif 1 <= opcion <= len(EJEMPLOS):
            _ejecutar_uno(EJEMPLOS[opcion - 1])
            return
        elif opcion == len(EJEMPLOS) + 1:
            for ej in EJEMPLOS:
                _ejecutar_uno(ej)
                input("  [Enter para continuar con el siguiente ejemplo...]")
            return
        else:
            print("  ✗ Opción fuera de rango.")


def _ejecutar_uno(ej):
    """Ejecuta y muestra un ejemplo."""
    sep = "─" * 60
    print(f"\n{sep}")
    print(f"  {ej['titulo']}")
    print(f"  {ej['descripcion']}")
    print(sep)

    if ej["tipo"] == "homogeneo":
        resolver_homogeneo(ej["orden"], ej["coefs"], ej["condiciones"])
    else:
        resolver_heterogeneo(
            ej["orden"], ej["coefs"], ej["condiciones"],
            ej["c"], ej["p"]
        )
