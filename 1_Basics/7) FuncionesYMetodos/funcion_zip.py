print("Funcion zip()")
print("-------------\n\n")

#La zip()función devuelve un objeto zip, que es un iterador de tuplas 
#donde el primer elemento de cada iterador pasado se empareja, y luego el segundo 
#elemento de cada iterador pasado se empareja, etc.

#Sintaxis: zip(iterator1, iterator2, iterator3 ...)
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")
x = list(zip(a, b))
print(x)
print("---")

nombres = ["Juan", "María", "Pedro"]
edades = [25, 30, 27]
ciudades = ["Madrid", "Barcelona", "Sevilla"]
profesiones = ["ingeniero", "abogada", "médico"]
print(list(zip(nombres, edades, ciudades, profesiones)))
for nombre, edad, ciudad, profesion in zip(nombres, edades, ciudades, profesiones):
    print(nombre, "tiene", edad, "años, vive en", ciudad, "y es", profesion)
