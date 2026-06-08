"""
main.py - Menú principal del solucionador de relaciones de recurrencia lineales.
"""

from parser_rec import leer_recurrencia
from homogeneo import resolver_homogeneo
from heterogeneo import resolver_heterogeneo
from ejemplos import ejecutar_ejemplos


BANNER = """
╔══════════════════════════════════════════════════════════════╗
║   SOLUCIONADOR DE RELACIONES DE RECURRENCIA LINEALES         ║
║   con coeficientes constantes  |  usando SymPy               ║
╚══════════════════════════════════════════════════════════════╝
"""

MENU = """
  [1] Resolver relación HOMOGÉNEA
  [2] Resolver relación HETEROGÉNEA (término = monomio c·nᵏ)
  [3] Ver ejemplos predefinidos
  [0] Salir
"""


def main():
    print(BANNER)
    while True:
        print(MENU)
        opcion = input("  Seleccione una opción: ").strip()

        if opcion == "1":
            print("\n── CASO HOMOGÉNEO ──────────────────────────────────────")
            datos = leer_recurrencia(heterogeneo=False)
            if datos:
                resolver_homogeneo(*datos)

        elif opcion == "2":
            print("\n── CASO HETEROGÉNEO (monomio) ──────────────────────────")
            datos = leer_recurrencia(heterogeneo=True)
            if datos:
                resolver_heterogeneo(*datos)

        elif opcion == "3":
            ejecutar_ejemplos()

        elif opcion == "0":
            print("\n  ¡Hasta luego!\n")
            break
        else:
            print("\n  Opción no válida. Intente de nuevo.")

        input("\n  Presione Enter para continuar...")


if __name__ == "__main__":
    main()
