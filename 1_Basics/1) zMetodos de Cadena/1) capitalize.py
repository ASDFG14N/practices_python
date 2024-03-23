#Convierte el primer carácter a mayúsculas
#Sintaxis: string.capitalize()
#no posee parametros.
print("Metodo Capitalize")
print("-----------------\n")

#Mayúsculas la primera letra de esta oración:
txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)

print()

#El primer carácter se convierte a mayúsculas y el resto se convierte a minúsculas:
txt = "python is FUN!"
x = txt.capitalize()
print (x)

print()

#Vea lo que sucede si el primer carácter es un número:
txt = "36 is my age."
x = txt.capitalize()
print (x)