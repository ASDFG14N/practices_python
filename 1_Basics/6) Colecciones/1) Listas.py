#Listas
#Una lista es un conjunto ordenado de valores, en el cual cada valor va identificado por un índice. 
# Los valores que constituyen una lista son sus elementos.
#Las listas son estructuras de datos que pueden almacenar cualquier otro tipo de dato,
#inclusive una lista puede contener otra lista, además, la cantidad de elementos de una lista se
#puede modificar removiendo o añadiendo elementos. Para definir una lista se utilizan los corchetes([])
#dentro de estos se colocan todos los elementos separados por comas:
#Se puede hacer una comparacion con Java pues una arrglo podria ser considerado a mi entendimiento como una lista.
#Se dice tambien que la funcion range es una lista
#El numero de elemntos es diferente del numero de posiciones de una lista, se cunta el numeor desde 0

#Creando una lista
print("Creando una lista")
print("-----------------")
calificaciones = [1,3,5,9,10]
nombres = ["Ana","Juan","Sofía","Pablo","Tania"]
mezcla = [True, 10.5, "abc", [0,1,1]]
print(nombres)
print(nombres[2])
print(calificaciones[3])
print(mezcla[3])


#Listas anidadas
print("Listas anidadas")
print("----------------")
lista = [1, "a", True, [1, 2, ["f", "g", "h"]]]
print(lista)
print(lista[0])
print(lista[3][1])
print(lista[3][2][1])