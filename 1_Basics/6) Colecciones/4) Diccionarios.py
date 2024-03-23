#Un diccionario es una estructura de datos cuyos componentes son pares llave/valor
#Un diccionario es una estructura que se utiliza para ordenar datos o elemntos,puede ser homogeneo o heterogene
# igual que las listas, asi mismo son mutables. su sintaxis es la siguiente: 
# nombre_diccionario = {llave: elemento}
# nombre_diccionario = {llave_1: elemnto1, llave_2: elemento2, ... llave_n: elmenton} #(varios elemntos)#
print("Diccionarios")
print("------------\n")

#La clase que defunbe que son los diccionarios, la forma de crearlos y los metodos para manejarlos es la clase
#dict. Para crearlos tendremos dos formas genericas 

print("Primera forma de crerar un diccionario") #mediante el formato de diccionario directamente
diccionario_vacio = {}  #diccionario vacio
print(diccionario_vacio)
print()
diccionario_1 = {1: "Juan", 8: "Eva"}
print(diccionario_1)
print()
diccionario_datos = {"name": "Brenda", "apellido" : "Flores", "años" : 22}
print(f"Diccionario de datos: {diccionario_datos}")
print()
diccionario_lista = {"a": {"a": 1}, "b": [1, 2, 3]}
print(f"Diccionario con lista y diccionario: {diccionario_lista}")
print()

print("Segunda forma de crear un diccionario") #Mediante el construcctor de la clase dict:
print(dict()) #diccionario vacio 
diccionario_constructor = dict(uno = 1, dos = 2, tres = 3)
print(diccionario_constructor)
print()

#acceder a, añadir y borrar elementos de diccionarios

#Para acceder a los datos de los diccionarios usaremos un formato similar al empelado en listas y tuplas,
#ahora el indice es un objeto hasheable.
#sintaxis ==> nombreDioccionario[llave]
alumnos = {1: "Juan", 2: "Eva", 3: "Carlos"}
print(alumnos[1], " y ", alumnos[3])
ciudades = {(1,1): "Madrid", (1,2): "Lima"}
print(ciudades[(1,2)])
#Para añadir o actualizar un nuevo elemento (entrada) a nuestor diccionario bastara con seguir el siguiente 
#fomrato, sintaxis ==> NombreDiccionario[llave] = valor
alumnos[10] = "Adan"
print(alumnos)
ciudades[(1,3)] = "Roma"
print(ciudades)
#Para eliminar un elemento del diccionario ussarmemos el formato: del NombreDiccionario[llave]
paises = {1: "Perú", 2: "Brazil", 3: "China"}
del paises[3]
print(paises)

#Operadores sobre dicionarios (in/not in; ==, !=)
print(4 in alumnos)
print(3 in alumnos)

#Funciones aplicadas a los diccionarios(len, max, min y sum)
diccionario_2 = {1: "Uno" , 2: "Dos", 3: "Tres", 4: "Cuatro"}
diccionario_3 = {5: "Cinco", 6: "Seis", 7: "Siete"}
print(len(diccionario_2), "y", len(diccionario_3)) #Numero de items en el diccionario
print(max(diccionario_2)) #imprime la llave mas grande de cada diccionario 
print(max(diccionario_3))
print(sum(diccionario_2)) #Suma las laves del diccionario