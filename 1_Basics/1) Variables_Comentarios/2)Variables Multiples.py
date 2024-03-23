print("Variables multiples")
print("-------------------\n")

#Python permite asignar valores a múltiples variables en una línea:
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z ,"\n")

#Si tiene una colección de valores en una lista, tupla, etc. Python le permite extraer los valores en 
# variables. Esto se llama desempacar .
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)