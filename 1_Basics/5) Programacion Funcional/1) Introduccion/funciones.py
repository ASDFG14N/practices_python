#las funciones son linea se codigo agrupadas que realizan una operacion, sirven para reciclar codigos.
#Se tienen que definir antes de ser usados
#Se puede llamar a una fucnion dentro de otra  es decir, se trabaja de manera recursuva
# si de define a una variable dentro de una funcion, no puede llamarse fuera de la funcion, pero si se define 
# la variable fuera de la fucnon y se llama a la funcion, si se puede hacer#
#Sintaxis ==> def nombre_de_la_funcion(lista de parametros formales):
                        #Bloque_de_instrucciones
#La lista de parametros formales(que puede estar vacia al no requerir datos de entrada) son los nombres de
#estos separados por comas. Se denominan parametros,
#El bloque de istrucciones prodra incluir(o no) una(o varias) return, que tiene el siguiente formato:
#       return valor_que_devuelve_una_funcion
print("\nFunciones en Python")
print("-------------------\n")

#Definiendo una funcion
def carta(): #No posee argumeto
    print("Hola amigo")
    print("Adios")
carta()
print()

#Ejemplo de funcion 2
def hola_mundo():
    nombre = "Gian"
    print("Hola mundo " + nombre)
hola_mundo()
print()

#Ejemplo 3
nombre2 = "Gian2"
def hola_mundo2():
    print("Hola mundo " + nombre2)
hola_mundo2()
print()

#Ejemplo 4
def saludo(nombre3):
    print("Hola " + nombre3)
saludo("Gian Arias")
print()

#Ejemplo 5
def suma(num1, num2):
    print(num1 + num2)
suma(5, 4)
print()

#Ejemplo 6
def resta(num1, num2):
    return num2 - num1
resultado_resta = resta(1, 9)
print(resultado_resta)
print()

#Ejemplo 7
def mostrar_Tabla(a, b):
    print(a, " x ", b, " = ", (a*b))
print(mostrar_Tabla(4, 2))
print()

#Ejemplo 8
#Funciones que retornan varios valores
def Suma_Resta(x, y):
    suma = x + y
    resta = x - y
    return suma, resta
r1, r2 = Suma_Resta(int(input("Introduce el primer valor: ")), int(input("Introduce el segundo valor: ")))
print("Los resultados son:\nSuma: " + str(r1) + "\nResta: " + str(r2))