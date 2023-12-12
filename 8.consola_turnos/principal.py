import numeros


def menu():
    print("Bienvenido a Farmacia Python")

    while True:
        print("[P] - Perfumería\n[F] - Farmacia\n[C] - Cosmútica")
        try:
            mi_rubro = input("Elija su rubro: ").upper()
            ["P", "F", "C"].index(mi_rubro)
        except ValueError:
            print("Esa no es una opción válida")
        else:
            break

    numeros.decorador_turnos(mi_rubro)


def inicio():
    while True:
        menu()
        try:
            otro_turno = input("Quieres sacar otro turno?: [S] [N]").upper()
            ["S", "N"].index(otro_turno)
        except ValueError:
            print("Esa no es una opción válida")
        else:
            if otro_turno == "N":
                print("Gracias por venir, que tenga buen día")
                break


inicio()
