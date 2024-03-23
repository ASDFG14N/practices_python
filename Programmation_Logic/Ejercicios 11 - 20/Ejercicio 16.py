#El número de sonidos emitidos por un grillo en un minuto es una función de la temperatura. 
# Como resultado de esto, es posible determinar el nivel de temperatura utilizando el grillo como termómetro.
#La fórmula de la función es: t = (N/4) + 10, donde t representa la temperatura en grados Fahrenheit y n 
#representa el número de sonidos emitidos en un minuto. Elabore un programa que determine e imprima los 
#valores para t cuando n toma los valores de 40, 50, 60, 70,…, 140, 150.
print("\tEjercicio 16")
print("\t------------\n")
def funcionT (n):
    t = (n/4) + 10
    return t
for i in range(40, 160, 10):
    print(f"El valor de [t], cuando [n] toma el valor de {i} es {funcionT(i)}")