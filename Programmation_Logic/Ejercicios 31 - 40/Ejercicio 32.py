#Realice un programa que sume los elementos de dos listas de números y guarde los valores en 
#una tercera lista. Ambas tienen la misma cantidad de elementos.

lista1 = [1, 2, 3, 4, 5]
lista2 = [1, 2, 3, 4, 5]
lista3 = []
elemento = 0
for i in range(0, len(lista1)):
    elemento = lista1[i] + lista2[i]
    lista3.append(elemento)
print(lista3)

