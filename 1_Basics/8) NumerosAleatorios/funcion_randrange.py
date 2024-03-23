#Esta funcion solo involucra numeros enteros#
#Sintaxis ==> random.randrange(cominezo, fianl, paso)
#Devuelve un numero entero aleatorio entre los numeros COMIENZO y FINAL, excluyendo este ultimo, pero solo
# elige entre los numeros que estén en la serie siguiente: 
# comienzo, comienzo + paso, comienzo + paso*2....#
import random
print("La funcion randrange()")
print("----------------------\n")

a = int(input("Introsuce un numero entero: "))
b = int(input("Introsuce un otro entero: "))
print(f"Los numeros {a} y {b} generan un numero: {random.randrange(a, b)} aleatorio")
print()

#esta funcion es mas compleja para tratar numeros enetros que la funcion randint(), ya que se puede emular a esta ultima
#de la siguiente manera:
#ramdom.randint(a, b) = random.randrange(a, b+1)
print("Emulando la funcion randint()\n")

print(random.randint(3, 7))
print(random.randrange(3, 8))
