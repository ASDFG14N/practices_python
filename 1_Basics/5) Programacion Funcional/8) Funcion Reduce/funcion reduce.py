from functools import reduce
numeros = [1,2,3,4,5,6]
imprimir = reduce(lambda x, y: x * y, numeros) 
print(imprimir)

#Las funciones reduce pueden servinos para calcular la MA
numeros1 = [1, 2, 3, 4, 5]
mediaAritmetica = reduce(lambda x, y: x + y, numeros1)
mediaAritmetica = mediaAritmetica / 5
print(mediaAritmetica)

#Usando una funcion
def mas_grade(a, b):
    if a > b:
        return a
    return b
numeros2 = [10, 5, 7, -3, -30, 2, 33]
variable = reduce(mas_grade, numeros2)
print(variable)