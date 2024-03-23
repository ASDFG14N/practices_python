#Disyunción
# Inicializamos la variable
numero = 10
# Ejecutamos el bucle mientras número sea diferente de 0
while not numero == 0:
    print(numero)
    numero -= 1
#Este bucle imprimirá los números del 10 al 1, ya que la condición not numero == 0 
#es verdadera mientras numero no sea igual a 0. Cuando numero llega a 0, la condición 
#se vuelve falsa y el bucle se detiene.
print()
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    if not number % 2 == 0:
        print(number)

