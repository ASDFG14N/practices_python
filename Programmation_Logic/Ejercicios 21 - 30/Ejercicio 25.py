#ORDENAR Y QUITAR ELEMENTOS REPETIDOS DEL VECTOR.
print("\tEjercicio 24")
print("\t------------\n")

vector = []

print("Ingrese el numero de elementos del vector")
elementos = int(input())

if 1 <= elementos and elementos < 100:
    for i in range(1, elementos+1):
        elemento = int(input(f"Ingrese el elementos de la posicion #{i}: "))
        vector.append(elemento)
print(vector)

listaNueva = []
for elemento in vector:
    #Si elemento no esta en la lista
    if elemento not in listaNueva:
        listaNueva.append(elemento)
print(listaNueva)

#ORDENAMOS LA NUEVA LISTA 
listaNueva.sort()
print(f"La nueva lista ordenada es: {listaNueva}")
