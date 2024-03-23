print("La funcion map()")
print("----------------\n\n")

#Ejemplo de uso: Imaginemos que tenemos una lista de enteros y se quiere obtener 
#una nueva lista con el cuadrado de cada uno de ellos.

#la primera opcion seria:
enteros = [1, 2, 3, 4, 5]
cuadrados = []
for exp in enteros:
    cuadrados.append(exp**2)
print(cuadrados)

print()

#Sin embargo podemos usar una funcion lambda en combinacion con map para obetner el mismo resultado
enteros2 = [1, 2, 3, 4, 5]
cuadrados2 = list(map((lambda x: x**2), enteros2)) 
print(cuadrados2)