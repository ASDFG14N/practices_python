#(Enteros menor y mayor) Escriba una aplicación que lea cinco enteros y que determine e imprima los enteros
#mayor y menor en el grupo. Use solamente las técnicas de programación que aprendió en este capítulo.

print("Ejercicio 5")
print("-----------\n")

lista = [] #Creamos una lista
for i in range(5): # Llenamos la lista con 5 elementos
    valor = int(input(f"Introduce el elemento numero {i+1}: "))
    lista.append(valor)
#Imprimimos los resultados
print("El maximo de los numero introducidos es:", max(lista))
print("El minimo de los numeros introducidos es:", min(lista))
