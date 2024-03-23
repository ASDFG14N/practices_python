#Definir una tupla con 10 edades de personas.
#Imprimir la cantidad de personas con edades superiores a 20.
#Puedes variar el ejercicio para que sea el usuario quien ingrese las edades.

tuplaEdades = (12, 3, 4, 27, 9, 15, 15, 7, 36, 43)
contador = 0
for i in tuplaEdades:
    if i > 20: contador = contador + 1
print("La cantidad de personas mayores a 20 es:", contador, "\n")

print("Ahora el usuario introduce las edades")
print("-------------------------------------")

lista = []
i = 0
contador = 0
while i < 10:
    lista.append(int(input(f"Agrega la edad de la persona #{i+1}: ")))
    i = i + 1
for iterador in lista:
    if iterador > 20:
        contador = contador + 1
print("La cantidad de personas mayores a 20 es:", contador)