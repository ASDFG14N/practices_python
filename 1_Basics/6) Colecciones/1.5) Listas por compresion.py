print("Listas por comprensipón")
print("-----------------------\n\n")

#La lista numeros = [1, 2, 3, 4, 5] se pude escribir de la siguiente menera.
numeros = []
for n in range(1, 6):
    numeros.append(n)
print(numeros)
#O la forma simplificada
#La primera n representa el elemento que se quiere incluir en la lista
listaComprension = [n for n in range(1, 6) ]
print(listaComprension)
