#Esta funcion solo involucra numeros enteros#
#Sintaxis ==> ramdom.randint(a, b)
#Devuelve un numero aleatorio entre los numero enteros a y b(incluso ambos).
import random
print("Funcion randint()")
print("-----------------\n")

a = int(input("Introduce un numero: "))
b = int(input("Introduce otro numero: "))
print(f"el numero entre {a} y {b} es {random.randint(a, b)}")