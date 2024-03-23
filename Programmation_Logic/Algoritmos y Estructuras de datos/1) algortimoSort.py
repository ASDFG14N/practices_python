#Implementa un algoritmo que ordene un arreglo de números enteros en orden ascendente 
#utilizando el algoritmo de ordenamiento por selección

def sort(lista):
    for i in range(len(lista)):
        min_idx = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]

#Inputs
lista_desordenada = [5, 8, 7, 1, 3, 6]
#Output
lista_ordenada = [1, 3, 5, 6, 7, 8]
sort(lista_desordenada)
print(lista_desordenada)