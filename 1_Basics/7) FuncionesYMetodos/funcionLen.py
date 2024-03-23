#Función len()
#esta funcion devuelve el numero de elementos de un objeto. El argumento puede ser una secuencia o una colección.
# sintaxis: len(objeto_iterable) 
print("Funcion len()")
print("-------------\n")

#Opción 1
print("Hola tiene", len("Hola"), "caracteres.")
#Opción 2
longitud = len("La Geekipedia")
print("La Geekipedia tiene", longitud, "caracteres")
a = [1, 2, 3, 4] #Lista
b = ('a', 'b', 'c') #Tupla
c = {1: 'a', 2: 'b'} #Diccionario
d = range(8) #Funcion range
print(a, ' -', len(a))
print(b, ' -', len(b))
print(c, ' -', len(c))
print(d, ' -', len(d))