#En programación, a menudo necesitas saber si una expresión es True o False.

print("Valores Booleanos")
print("-----------------\n")

#Cuando compara dos valores, la expresión se evalúa y Python devuelve la respuesta booleana:
print(10 > 9) #10 es mayor que 9 (True)
print(10 == 9) #10 no es igua a 9 (False)
print(10 < 9) #10 es menor a nueve (False)

print()

#Cuando ejecuta una condición en una declaración if, Python devuelve Trueo False:
#Ejemplo: Imprime un mensaje basado en si la condición es Trueo False:
a = 200
b = 33
if b > a: #Si b es mayor que a, hacer las intrucciones: 
  print("b es mayor que a")
else:
  print("b no es mayor que a")

print()

#La bool() función te permite evaluar cualquier valor, y darte True o False a cambio, 
#Evaluar una cadena y un número:
print(bool("Hello"))
print(bool(15))

print()

#Las funciones pueden devolver un valor booleano
#Imprime la respuesta de una función:
def myFunction() :
  return True
print(myFunction())

print()

#Imprimir "¡SÍ!" si la función devuelve True, de lo contrario imprime "¡NO!":
def myFunction2() :
  return True
if myFunction2():
  print("Yes")
else:
  print("No!!")