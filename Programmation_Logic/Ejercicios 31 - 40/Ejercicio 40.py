#Crea una función (cantidad_pares) que cuente la cantidad de números pares que existen 
#en una lista (lista_numeros), y devuelva el resultado de dicha suma.
print("\tEjercicio 38")
print("\t------------\n")

def cantidad_pares(lista_numeros):
    sumaPares = 0
    for n in lista_numeros: 
        if n % 2 == 0: sumaPares = sumaPares + n
    return sumaPares
lista_numeros = [6, 8, 7, 10, 12, 14, 65, 32, 20, 5, 2]
print(f"La suma de los numeros pares encontrados en la lista es: {cantidad_pares(lista_numeros=lista_numeros)}")