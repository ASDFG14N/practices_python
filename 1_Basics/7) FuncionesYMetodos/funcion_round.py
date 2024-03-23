from math import pi
a = 10 / 3
b = 20.7 / 3
# By default, Python outputs many digits after decimal point for real numbers.
#(Por defecto, Python genera muchos digitos despues del punto decimal para los numeros reales)
print(a)
print(b)
print(pi)
print()
# round() without a second argument rounds to the nearest integer
#(la funcion reound() sin un segundo argumento redondea al entero más cercano)
print(round(a))
print(round(b))
print(round(pi))
print()
# The second argument indicates the number of digitsb after the decimal point
#(El segundo argumento indica el numero de digitos despues del punto decimal)
print(round(a, 2))
print(round(b, 2))
print(round(pi, 4))
