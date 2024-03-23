import math
print("Parte entera de un numero")
print("-------------------------\n\n")

print("El metodo floor")
print("---------------")
#Este metodo redontede a la parte mas pequeña y entera de un numero.
x = 2.8451
print(math.floor(x)) #salida 2
x1 = -57.191
print(math.floor(x1)) #salida -58

print()

print("El metodo ceil")
print("--------------")
#El numero entero es mayor o igual
print(math.ceil(x))
print(math.ceil(x1))

print()

print("El metodo trunc")
print("---------------")
#Quita todo lo que viene despues de la coma
print(math.trunc(x))
print(math.trunc(x1))