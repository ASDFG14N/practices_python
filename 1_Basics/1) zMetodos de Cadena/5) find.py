#Busca en la cadena un valor específico y devuelve la posición donde se encontró
#El find()método encuentra la primera aparición del valor especificado.
#Sintaxis: string.find(value, start, end)
print("Metodo Find")
print("-----------------\n")

#¿En qué parte del texto aparece por primera vez la letra "e"?:
txt = "Hello, welcome to my world."
x = txt.find("e")
print(x)

print()

#¿En qué parte del texto aparece por primera vez la letra "e" cuando solo busca entre la posición 5 y 10?:
txt = "Hello, welcome to my world."
x = txt.find("e", 5, 10)
print(x)

print()

#Si no se encuentra el valor, el método find() devuelve -1.
txt = "Hello, welcome to my world."
print(txt.find("q"))