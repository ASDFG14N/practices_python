#En Python for se utiliza como una forma genérica de iterar sobre una secuencia.
#El bucle for, en Python, es aquel que nos permitirá iterar sobre una variable compleja, del tipo lista o tupla

#Sintaxis
# for VARIABLE in OBJETO_ITERABLE:
     #identacion(instrucción)
#Objeto iterable: pertime recorrer sus elementos uno a uno, ejemplo: cadena de caracteres 

#0
string = "Hola Gian"
for caracter in string:
    print(caracter)
print("Fin del ejemplo 0")
#1. Por cada nombre en mi_lista, imprimir nombre
mi_lista = [1,2,3]
for numero in mi_lista:
    print(numero)
print("Fin del programa 1")

mi_lista2 = [1,2,3,4,5,6,7,8,9,10]
for numero in mi_lista2:
    #Chequear numero pares
    if numero % 2 == 0:
        print(numero)
    else:
        print(f"Numero impar: {numero}")
print()

#2. Por cada color en mi_tupla, imprimir color
mi_tupla = ("azul", "amarillo", "verde")
for color in mi_tupla:
    print(color)
print()

#3. el bucle for, puede emular a while:
for año in range(2020, 2022):
    print("Año", str(año))