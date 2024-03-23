#Devuelve True si todos los caracteres de la cadena están en minúsculas
#El islower()método devuelve True si todos los caracteres están en minúsculas, de lo contrario False.
#Los números, símbolos y espacios no están marcados, solo los caracteres alfabéticos.
#Sintaxis: string.islower(), no tiene parametros
print("Metodo islower")
print("--------------\n")

#Comprueba si todos los caracteres del texto están en minúsculas:
txt = "hello world!"
x = txt.islower()
print(x)

print()

#Comprueba si todos los caracteres de los textos están en minúsculas:
a = "Hello world!"
b = "hello 123"
c = "mynameisPeter"

print(a.islower())
print(b.islower())
print(c.islower())