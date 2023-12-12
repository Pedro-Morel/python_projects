def turnos_perfumeria():
    for n in range(1, 1000):
        yield f"P: {n}"


def turnos_farmacia():
    for n in range(1, 1000):
        yield f"F: {n}"


def turnos_cosmetica():
    for n in range(1, 1000):
        yield f"C: {n}"


p = turnos_perfumeria()
f = turnos_farmacia()
c = turnos_cosmetica()


def decorador_turnos(rubro):
    print("\n" + "*" * 10)
    print(f"Su turno es:")
    if rubro == "P":
        print(next(p))
    elif rubro == "F":
        print(next(f))
    elif rubro == "C":
        print(next(c))
    print("Aguarde su turno, será atendido")
    print("\n" + "*" * 10)
