#Hacer un algoritmo que muestre un menú y permita elegir al usuario cuál de las cuatro operaciones 
#aritméticas básicas quiere hacer: suma, resta, multiplicación y división (incluir opción para salir).
print("\tEjercicio 15")
print("\t------------\n")

numero = 0
print("¿Que operacion aritmetica deseas realizar?, introduce un numero\n")
print("1) Suma")
print("2) Resta")
print("3) Multiplicacion")
print("4) Division")
numero = int(input("Aqui el numero: "))
if numero == 1:
    numero = int(input("Ingresa el primer numero: "))
    numero = numero + int(input("Ingresa el segundo numero: "))
    print("La suma es:", numero)
if numero == 2:
    numero = int(input("Ingresa el primer numero: "))
    numero = numero - int(input("Ingresa el segundo numero: "))
    print("La resta es:", numero)