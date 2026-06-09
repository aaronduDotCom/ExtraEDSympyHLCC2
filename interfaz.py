def mostrar_resultado(resultado):

    print("\n========================")
    print("RESULTADO")
    print("========================")

    print("\nTipo de raíces:")
    print(resultado["tipo"])

    print("\nRaíces:")

    for r in resultado["raices"]:
        print(r)

    print("\nα =", resultado["alpha"])
    print("β =", resultado["beta"])

    print("\nSolución cerrada:")

    print("f(n) =", resultado["solucion"])