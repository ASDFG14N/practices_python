#Este metodo permite ordenar una lista, de manera ascendete o descendente, es posible pasarle un argumento
#para que la lista vaya de mayor a menor, por el contrario si no se le pasa nada al argumento el metodo ordenará
#la lista de menor a menor.
#SINTASIS: nombre_lista.sort() o bien nombre_lista.sort(reverse = true)
#no importa el tipo de dato
print("Metodo sort()")
print("-------------")
numeros = [1, 8, 9, 6, 2, 3]
vocales = ["e", "a", "i", "o", "u"]
print(f"Lista numeros: {numeros}")
numeros.sort()
print(f"\nLista numeros ordenada: {numeros}")
numeros.sort(reverse = True)
print(f"Lista ordenanda de menor a mayor: {numeros}")

vocales.sort()
print(f"\nLista vocales ordenada: {vocales}")
vocales.sort(reverse=True)
print(f"Lista vocales al reves: {vocales}")