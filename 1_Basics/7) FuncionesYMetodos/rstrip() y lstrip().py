#Método rstrip
print("Método rstrip")#Solo busca los elemntos a eliminar desde el final.
cadena = "\tHola Ernesto\n"
print(cadena)

cadena = cadena.rstrip("s tHo\t\n")
print(cadena)
print()

#Método lstrip
print("Método lstrip")#Solo busca los elemntos a eliminar desde el inicio
cadena = "\tHola Ernesto\n"
print(cadena)

cadena = cadena.lstrip("s tHo\t\n")
print(cadena)