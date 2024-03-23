#La idea es importar ficheros(contenerdores de funciones), para evitar reescribir codigo innesesariamente
# un modulo puede contener muchas funciones o solo una funcion.
# Para cargar estos ficheros y por tanto tener acceso a las funciones que contienen, usaremsos la palabra reservada IMPORT.
# su formato es el siguiente ==> import nombre_del_modulo #
#EJEMPLO
import math
#lUEGO == para usar las funciones de la libreria math basta con poner un punto y el nombre de la funcion
print(math.factorial(3))
print()

x = int(input("Introduce un numero para realizar la operacion: "))
#calculo
print(math.pow(x, 8,) + (2*math.sin(x)) + math.factorial(x))

#La forma abreviada de nombrar a un modulo es ==> import nombre_del_modulo as nuevo_nombre_de_referencia 