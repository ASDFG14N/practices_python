#Implementa para la siguiente función cociente(), un manejador de errores:

    #Ante un error de tipo (TypeError), debe imprimir en pantalla el mensaje: "Los argumentos a ingresar deben ser números"

    #Si se generara una división por cero (error del tipo ZeroDivisionError), el mensaje mostrado debe ser: "El segundo 
    #argumento no debe ser cero"

#En caso que no se produzca un error, deberá limitarse a imprimir el resultado del cociente (división) entre los 
#dos números entregados como argumento.
def cociente():
    numeroUno = int(input("Ingresa el primer numero: "))
    numeroDos = int(input("Ingresa el segundo numero: "))
    cociente = numeroUno / numeroDos
    print("La division es:", cociente)
try:
    cociente()
except TypeError:
    print("Los argumentos a ingresar deben ser números")
except ZeroDivisionError:
    print("El segundo argumento no sebe ser cero")
except ValueError:
    print("Eso es una letra debe ser numero")