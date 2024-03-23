#Numero arbitrario de numeros: 
#Si no sabemos el numero de parametros que van a ser introducucidos, añadimos un "*" previo al nombre del 
#parametro en la definicion de la funcion, los valor introducidos seran guardados en una tupla.
def sum_numeros(*numeros):
    suma = 0
    for n in numeros:
        suma = suma + n
    return suma
def main():
    suma = sum_numeros(8, 7, 1)
    print("La suma es:", suma)
main()
    