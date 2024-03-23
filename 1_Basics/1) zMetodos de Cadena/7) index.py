#Busca en la cadena un valor específico y devuelve la posición donde se encontró
#El index()método encuentra la primera aparición del valor especificado.
#Sintaxis: string.index(value, start, end)

print("Metodo Index")
print("-----------------\n")

#¿En qué parte del texto aparece por primera vez la letra "e"?:
txt = "Hello, welcome to my world."
x = txt.index("e")
print(x)

print()

#¿Dónde en el texto está la palabra "bienvenido"?:
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)

print()

#¿En qué parte del texto aparece por primera vez la letra "e" cuando solo busca entre la posición 5 y 10?:
txt = "Hello, welcome to my world."
x = txt.index("e", 5, 10)
print(x)

print()

#Si no se encuentra el valor, el método find() devuelve -1, pero el método index() generará una excepción:
txt = "Hello, welcome to my world."
print(txt.find("q"))
print(txt.index("q"))