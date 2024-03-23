#Primera alternativa
nombre = "GianASDF"
edad = 20 
print ("Hola {} tienes {} años.".format(nombre, edad))
print("--------------------------\n")
#Segunda alternativa
print ("Hola {nombre1} tienes {edad1} años.".format(nombre1 = "GianASDF", edad1 = 20))
print("--------------------------\n")
#Tercer metodo
nombre2 = "GianASDF"
edad2 = 20 
print ("Hola {1} tienes {0} años.".format(edad2, nombre2))
print("--------------------------\n")
#Metodo del libro xd
a = "{} {}!"
print(a.format('Hola', 'World'))
print(a.format('Hola', 'Gian'))

print("--------------------------")

a = "apple{1}, orange{0}"
print(a.format(333, 888))

print("--------------------------")

a = "a{apple}, o{orange}"
print(a.format(apple=4, orange=1))
print(a.format(orange=1, apple=4))

print("--------------------------")

a = "fraction {:.3}"
print(a.format(12/7))

print("--------------------------")

a = "{0:b}"
print(a.format(34))