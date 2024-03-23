#Devuelve el número de veces que aparece un valor especificado en una cadena, objetos iterables
#Sintasis: string.count(value, start, end)
#value: Requerido. Una cuerda. La cadena al valor a buscar
#start: Opcional. Un entero. La posición para iniciar la búsqueda. El valor predeterminado es 0
#end: Opcional. Un entero. La posición para finalizar la búsqueda. El valor predeterminado es el final de la cadena.

print("Metodo Count")
print("-----------------\n")

#Devuelve el número de veces que aparece el valor "apple" en la cadena:
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)

print()

txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple", 10, 24)
print(x)