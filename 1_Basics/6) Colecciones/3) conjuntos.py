#Los conjuntos almacenan una serie de datos, como en las listas o tuplas, pero en contraposicion a estas no lo hacen#
# siguindo un orden, por lo que no se accede a ellos mediante uno a varios indices, ya que no estan ubicados 
# en algun lugar en concreto, adema sno se permiten elementos repetidos, corresponde a los conjuntos en metematicas# 
#los conjuntois son mas rapidos que una lista y una tupla, en nuestros programas iran a gran velocidad

#sintasis==> {dato1, dato2, dato3, dato4, ....}

#los datos no tienen que ser obligatoriamente de mismo tipo, pero si es obligatorio que sean hasheable, esto
#es que tienen un valor que los identifica, por lo que ese valor no puede cambiar.

print("\nColecciones - conjuntos")
print("-----------------------\n")

#Formas de crear un conjunto

print("Pimera forma\n")
conjuntoValoresEnteros = {1, 2, 21, 7} #conjunto de valores enteros 
print(conjuntoValoresEnteros)
conjuntoValoresHeterogeneos = {1, 3.14, "Hola"} #conjunto de valores heterogeneos
print(conjuntoValoresHeterogeneos)
conjuntoValoresHeterogeneos2 = {12, 3.98, (6,2), (1,11), "Hola"}
print(conjuntoValoresHeterogeneos2)
conjuntoElementosRepetidos = {1, 1, 1, 1, 1, 2, 2, 3 , 1} #los elementos repetidos solo se representan una vez
print(conjuntoElementosRepetidos)
#Si dejamos un cojunto vacio estariamos creando un diccionario vacio, tener cuidado
print()

print("Segunda forma\n")
#mediante el constructor de la clase set que tiene la sintaxis ==> set([iterable])
#Nos devuelve un conjuntio cuyos elementos son los propios del iterable pero con las caracteristicas propias
#de los cojuntos, como el no poder tener elementos repetidos
conjunto0 = set() #conjunto vacio
print(conjunto0)
conjunto1 = set([1, 2, 3]) #Conjunto a partir de una lista
print(conjunto1)
conjunto2 = set((4, 5, 6)) #conjunto a partir de una tupla
print(conjunto2)
conjunto3 = set("Frese de prueba") #conjunto a partir de una cadena te texto
print(conjunto3)
print()

#Operadores sobre conjuntos(|(alt+124), ^(alt+94) &, -, in, not in, <, <=, >, >=, ==, !=)
#UNION(|): crea un conjunto con todos los elementos tanto de A como de B
#Interseccion (&): definicion matematica
#Diferencia(-): crea un conjunto con los elementos de A exceto los de B incluyendo la interseccion
#Diferencia simetrica (^): definicion matematica
print("Operaciones sobre conjuntos\n")

A = {1, 2, 3, "Hola", 21, (7, 12)}
print(A)
B = {"a", "b", 100, "Hola", 21, (7, 12)}
print(B)
print(f"Union de los conjuntos A y B es: {A|B}")
print(f"Interseccion de los conjuntos A y B es: {A&B}")
print(f"Diferencia de los conjuntos A y B es: {A-B}")
print(f"Diferencia simetrica de los conjuntos A y B es: {A^B}")
print()

#Funciones plicadas a los conjuntos len(), max(), min(), sum()
