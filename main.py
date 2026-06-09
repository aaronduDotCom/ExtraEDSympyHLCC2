from recurrencia import resolver_hlcc2
from interfaz import mostrar_resultado
from ejemplos import fibonacci, ejemplo_raiz_repetida


def menu():

    while True:

        print("\n===== SOLVER HLCC(2) =====")
        print("1. Resolver recurrencia")
        print("2. Fibonacci")
        print("3. Ejemplo raíz repetida")
        print("4. Salir")

        opcion = input("\nSeleccione: ")

        if opcion == "1":

            a = int(input("a = "))
            b = int(input("b = "))
            f0 = int(input("f0 = "))
            f1 = int(input("f1 = "))

            resultado = resolver_hlcc2(a, b, f0, f1)

            mostrar_resultado(resultado)

        elif opcion == "2":
            fibonacci()

        elif opcion == "3":
            ejemplo_raiz_repetida()

        elif opcion == "4":
            break

        else:
            print("Opción inválida")


menu()