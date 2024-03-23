#(Tabla de cuadrados y cubos) Utilizando sólo las técnicas de programación que aprendió en este capítulo,
#escriba una aplicación que calcule los cuadrados y cubos de los números del 0 al 10, y que imprima los valores 
#resultantes en formato de tabla, como se muestra a continuación.
print("Ejercicio 7")
print("-----------\n")
contador = 0
while contador < 11:
    print(f"{contador} elevado al cuadrado es:", contador*contador)
    contador = contador + 1
contador = 0
print()
while contador < 11:
    print(f"{contador} elevado al cubo es:", contador*contador*contador)
    contador = contador + 1
