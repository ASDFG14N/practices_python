#Elabore los algoritmos para hacer e imprimir una cantidad predeterminada
#de términos de las siguientes sucesiones numéricas.
#3, 6, 5, 8, 7, 10, 9,...
#1, 4, 1, 8, 3, 12, 5, 16, 7, 20,…
#3, 6, 9, 12, 15, 36, 21, 24, 81, 30,…
print("\tEjercicio 30")
print("\t------------\n")

print("Primera serie:")
num1 = 3
num2 = 0
while num1 <=24:
    num2 = num1 + 3
    print(num1, num2, end=" ")
    num1 = num2 - 1

print("\n\nSegunda serie")
#1, 4, 1, 8, 3, 12, 5, 16, 7, 20, 9, 24, 11, 28, 13

num1 = 1
num2 = 4
num3 = 1
while num1 <= 20:
    num4 = num2 + 4
    print(num1, num2, num3, num4, end=" ")
    num1 = num3 + 2
    num2 = num4 + 4
    num3 = num1 + 2


