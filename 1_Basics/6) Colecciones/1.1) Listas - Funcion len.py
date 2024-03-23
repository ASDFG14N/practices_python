#Longitud o tamaño de una lista(usamos la funcion len() )
#La función len toma una lista y devuelve su tamaño. Es una buena idea usar este valor como límite }
# superior de un bucle, en lugar de una constante.
print("Longitud o tamaño de una lista usando la funciona len(): ")
print("---------------------------------------------------------")

arreglo = [5,9,6,8,10,20,15,4,1] #la funcion len() cuenta desde el numero 1
print("el arreglo tiene una longitud de: ", len(arreglo))

print()

print("usamos el bucle for")
for i in arreglo:
    print(arreglo[5])
print("usamos el bulce while para hacer el mismo trabajo que el bucle for:")
contador = 0
while contador<len(arreglo):
    print(arreglo[5])
    contador = contador + 1