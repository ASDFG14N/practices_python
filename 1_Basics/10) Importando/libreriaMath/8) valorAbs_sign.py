import math
print("valor absoluto")
print("--------------\n")
#Para calcular el valor absoluto de un numero usamos el metodo fabs()
x = -2.681
print(math.fabs(x))

print("Signo")
print("-----\n")
#Dados dos numeros reales x e y, si usamos el metodo .copysign() obtenemos como resultado el valor
#absoluto del primer parametro introducido, pero con el signo del segundo parametro
a = -25.6
b = -73
print(math.copysign(a, b))