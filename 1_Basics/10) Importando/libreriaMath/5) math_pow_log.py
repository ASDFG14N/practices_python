import math
print("Potencias y logaritmos")
print("----------------------\n\n")

#El metodo exp nos devuelve el numero e a la "x"
print(math.exp(2)) #Salida e al cuadrado

#El metodo expm1 devuelve el resultado de e a la "x" menos 1
print(math.expm1(2))

#El metodo .frexp() de un "x" nos devuelve el par(m, e) donde x = m * 2 ^ e
x = 25
m, e = math.frexp(x)
print("m = {}, e = {}".format(m, e))

#El metodo .ldexp() es el metodo inverso al anterior, introducicmos, m y e y devuelve x
a = 0.78125 # este sera m
i = 5 #Este sera la e
print(math.ldexp(a, i)) #Imprime x que seria 25

print("\nLogaritmos")

#EL metodo log() devuelve diferentes resultados segun los argumentos
#»Si solamente indicamos el numero, entonces el metodo calculara el logaritmo neperiano
#»Si introducimos dos parametros, el primero sera el numero y el segundo la base

#Logaritmo neperiano de 55
print(math.log(55))
#Logarimo en base 10 de 100
print(math.log(100, 10))

#El metodo .log1p() devuelve el logaritmo neperiano  de x + 1
#Este metodo aumenta la presisicion del resultado cuando x es proximo a 0
print(math.log1p(2))

#El metodo pow nos calcula la potencia de x a la y.
print(math.pow(2, 3))

#El metodo sqrt nos devuelve la raiz cuadrada de un numero entero n
print(math.sqrt(25))

