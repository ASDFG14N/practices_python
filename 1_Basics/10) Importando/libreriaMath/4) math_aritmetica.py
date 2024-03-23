import math
print("Aritmetica")
print("----------\n\n")
#El metodo fmod es similar al simbolo de porcentaje pero permite usar flotantes
x = 5.25
y = 2.5
print(math.fmod(x, y))

#El metodo fsum permite sumar todos los elementos de un objeto iterable, usta puntop flotante
lista = [0.5, 0.8, 4, 6.2]
print(f"El resultado de la suma de la lista es: {math.fsum(lista)}")

#El metodo .modf permitr separar la parte decimal y entera de un numero y ordenarlo en una tupla
print(math.modf(4.25))

