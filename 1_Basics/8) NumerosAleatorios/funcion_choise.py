#esta funcion solo funciona con cadenas de caracteres
#Devuelve un elemento indicidual aleatorio incluido en la cadena CADENA
#Sintaxis ==> random.choise(cadena)
import random
print("Funcion choise()")
print("--------------\n")

cadena = input("Introduce una cadena de texto: ")
print(f"La letra elegida de {cadena} es {random.choice(cadena)}")