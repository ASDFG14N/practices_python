print("\tEjericio 42")
print("\t-----------\n\n")

#La funcion debe eliminar elementos duplicados de la lista y eliminar el valor mas alto
def reducir_lista(lista_numeros):
    lista_numeros= set(lista_numeros)
    """
    for elemento in lista_numeros:
        if not elemento in nueva_lista:     <== esta es otra manera de hacer la linea 6
            nueva_lista.append(elemento)
    """
    lista_numeros = [x for x in lista_numeros if x != max(lista_numeros)] #Lista por comprensión
    #Se lee {x/ por cada x en nuevalista, si x != de valor_maximo}, se agrea a la lista
    # se compone de [expresion      for elemento    in iterable]
    #               [x**2           for x           in range(1, 10)]
    return lista_numeros
lista_numeros = [1, 2, 15, 7, 8, 9, 9, 50, 2]
print(reducir_lista(lista_numeros=lista_numeros))