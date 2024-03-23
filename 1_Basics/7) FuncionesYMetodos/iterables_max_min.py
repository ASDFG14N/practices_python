print("Metodo min() y max()")
print("--------------------")

a = [2, 6, 0, -3, 5] #Lista
print(f"la primera lista es: {a}")
b = ['a', 'bc', 'de', 'z', 'fff'] #Lista
print(f"la segunda lista es: {b}\n")
# If one argument is passed, it must be an iterable object.(Si se pasa un argumento, debe ser un objeto iterable)
# Functions return its smallest and largest elements, respectively.
# Las funciones devuelven sus elementos más pequeño y más grande, respectivamente.
#Sintaxis min(objeto_iterable), max(objeto_iterable)
print(f"el minimo valor de la lista a es: {min(a)} y el maximo valor de la lista a es: {max(a)}")
print(f"el minimo valor de la lista a es: {min(b)} y el maximo valor de la lista b es: {max(b)}")
print('----------------------------------------------------------------------------------------')
# If several objects are transmitted, then the minimum or maximum of them is returned.
# Si se transmiten varios objetos, se devuelve el mínimo o el máximo de ellos.
m = min(1, -1, 8, 0) #Tuplas
print(m)
print('--------')
# In this case, iterable objects are compared. (# En este caso, se comparan los objetos iterables.)
a = [2, 6, 0, -3, 5]
b = [19, 14, 18]
# Here, the max() function will return an entire list whose first element is larger.
# Aquí, la función max() devolverá una lista completa cuyo primer elemento es más grande.
print(max(a, b))
# The min() and max() functions can also take a key argument. It should be a function.
# Las funciones min() y max() también pueden tomar un argumento clave. Debería ser una función.
# In this case, will return the list, the sum of the elements of which is less.
# En este caso, devolverá la lista cuya suma de elementos es menor.
print(min(a, b, key=sum))
