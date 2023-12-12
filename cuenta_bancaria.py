class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):

    def __init__(self, nombre, apellido, numero_cuenta, balance = 0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"Nombre: {self.nombre} \nApellido: {self.apellido} \nNúmero de cuenta: {self.numero_cuenta} \nBalance: ${self.balance}"

    def depositar(self, deposito):
        self.balance += deposito
        print("Deposito hecho correctamente")

    def retirar(self, retiro):
        if self.balance <= retiro:
            print("No tiene esa cantidad de dinero")
        else:
            self.balance -= retiro
            print("Retiro realizado correctamente")


def crear_cliente():
    nombre_cliente = input(f"Ingrese su nombre: ")
    apellido_cliente = input(f"Ingrese su apellido: ")
    numero_cuenta = input(f"Ingrese su número de cuenta: ")
    cliente = Cliente(nombre_cliente, apellido_cliente, numero_cuenta)
    return cliente


def menu():
    mi_cliente = crear_cliente()
    print(mi_cliente)
    opcion = 0

    while opcion != 4:

        print("\t.:Menu:.")
        print("1. Ingresar dinero en la cuenta")
        print("2. Retirar dinero de la cuenta")
        print("3. Mostrar dinero disponible")
        print("4. Salir")
        opcion = int(input("Digite una opción del menu: "))

        if opcion == 1:
            deposito = int(input("ingrese el monto a depositar: "))
            mi_cliente.depositar(deposito)
        elif opcion == 2:
            retiro = int(input("Ingrese el monto a retirar: "))
            mi_cliente.retirar(retiro)
        elif opcion == 3:
            print(mi_cliente)
        elif opcion == 4:
            print("Hasta luego, que tenga buenos días")
        print(mi_cliente)
    print("Gracias por operar en su banco de confianza")


menu()