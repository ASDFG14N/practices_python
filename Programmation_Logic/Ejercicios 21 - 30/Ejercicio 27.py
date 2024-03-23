#Obtener un algoritmo que permita capturar un numero indefinida de valores diferentes
#y que los muestre ordenados de mayor a menor.
print("\tEjercicio 27")
print("\t------------\n")

centinela = -60
contador = 0
lista = []
numero = 0
while numero != centinela:
    numero = int(input(f"Ingrese el valor #{contador + 1}(-60 para terminar): "))
    if numero != centinela:
        lista.append(numero)
    contador = contador + 1

alternativa = int(input("¿Desea ordenar los numeros de manera ascendente(1) o descendente(2): "))
if alternativa == 1:
    lista.sort()
    print("El orden de la lista de manera ascendnete es: ")
    for i in lista:
        print(i)
elif alternativa == 2:
    lista.sort(reverse=True)
    print("El orden de la lista de manera descendente es: ")
    for i in lista:
        print(i)
else:
    print("La alternativa elegida no existe")


    
