#Crea una función (suma_menores) que sume los números de una lista 
#(almacenada en la variable lista_numeros) siempre y cuando sean mayores a 0 y menores a 1000, 
#y devuelva el resultado de dicha suma.
print("\tEjercicio 39")
print("\t------------\n\n")
def suma_menores(lista_numeros):
    suma = 0
    for n in lista_numeros:
        if n > 0 and n < 1000:
            suma = suma + n
    return suma
lista = [10, 14, 66, 84, 600, 978, 1005, 20121]
print(f"La suma total de la lista es: {suma_menores(lista_numeros=lista)}")