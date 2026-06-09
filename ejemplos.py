from recurrencia import resolver_hlcc2
from interfaz import mostrar_resultado


def fibonacci():

    print("\n===== FIBONACCI =====")

    resultado = resolver_hlcc2(
        a=1,
        b=1,
        f0=0,
        f1=1
    )

    mostrar_resultado(resultado)


def ejemplo_raiz_repetida():

    print("\n===== RAÍZ REPETIDA =====")

    resultado = resolver_hlcc2(
        a=6,
        b=-9,
        f0=2,
        f1=6
    )

    mostrar_resultado(resultado)