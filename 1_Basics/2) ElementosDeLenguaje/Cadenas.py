print("Cadenas")
print("-------\n")

#Cadenas multilineas
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

print()

#Comprobar cadena
#Ejemplo: Compruebe si "gratis" está presente en el siguiente texto:
txt = "The best things in life are free!"
print("free" in txt)

#Usando la instruccion if
#Ejemplo Obtenga su propio servidor Python Imprima solo si "gratis" está presente:
txt = "The best things in life are free!"
if "free" in txt: #Condicion de falsedad o verdad
  print("Yes, 'free' is present.")

#Ejemplo: Para verificar si una determinada frase o carácter NO está presente en una cadena, podemos usar 
# la palabra clave not in.
txt = "The best things in life are free!"
print("expensive" not in txt) #Retorna valores booleanos