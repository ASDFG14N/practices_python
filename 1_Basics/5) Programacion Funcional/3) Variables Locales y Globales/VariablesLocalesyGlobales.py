#¿Que hay de diferencia hay entre variables globales y locales? Para entender bien esto debemos ser conscientes
#de como tenemos estructurado nuestro programa#
#Cuando varios trozos de codigo se comunican, es en esencia la PROGRAMANCION FUNCIONAL: dividir el programa en 
#funciones que se comunican unas con otras.
#Decimos entocenes que:
#VARIABLES LOCACES: son varaibles definidas dentro de una funcion y que tiene como ambito de actuacion solo la
                   #propia funcion.
#VARIABLES GLOBALES: su ambito de utilizacion es todo el programa, por lo que puede ser usada en cualquier
                    #funcion
x = 5 #Esta es una variable global y sera accesible por cualquiera de las dos funciones
def funcion2():
    print("La variable x dentro de la funcion2 vale: ", x)
def main():
    funcion2()
    print("La variable x dentro de main vale: ", x)
main()