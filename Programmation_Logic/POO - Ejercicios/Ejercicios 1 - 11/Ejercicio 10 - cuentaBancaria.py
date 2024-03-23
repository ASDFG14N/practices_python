class Persona():
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
#La clase cliente hereda la clase persona, es decir, sus atributos
class Cliente (Persona):
    def __init__(self, nombre, apellido, numeroCuenta, balance = 0): #Construstor de la clase cliente
        super().__init__(nombre, apellido)
        self.numeroCuenta = numeroCuenta
        self.balance = balance
    #Metodos especiales de la clase
    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}\nBalance de cuenta {self.numeroCuenta}: ${self.balance}"
    def depositar(self, montoDeposito):
        self.balance += montoDeposito
        print("Deposito aceptado")
    def retirar(self, montoRetiro):
        if self.balance >= montoRetiro:
            self.balance -= montoRetiro
            print("Retiro realisado")
        else:
            print("Fondos insuficientes")
#Funcion que va a crear un nuevo cliente
def crearCliente():
    nombre_cl = input("Ingresa tu nombre: ")
    apellido_cl = input("Ingresa tu apellido: ")
    numero_cuenta = input("Ingrese su numero de cuenta: ") 
    #Creamos una instancia de la clase cliente
    cliente = Cliente(nombre=nombre_cl, apellido=apellido_cl, numeroCuenta=numero_cuenta)
    return cliente
def main():
    miCliente = crearCliente()
    print(miCliente)
    opcion = 0
    while opcion != "S":
        print("Elige: Depositar (D), Retirar (R) o Salir (S)")
        opcion = input()
        if opcion == "D":
            montoDeposito = int(input("Monto a depositar: "))
            miCliente.depositar(montoDeposito=montoDeposito)
        elif opcion == "R":
            montoRetiro = int(input("Monto a retirar: "))
            miCliente.retirar(montoRetiro=montoRetiro)
        print(miCliente)
    print("Gracias por operar :)")
main()