#Crear una lista, por comprension que contenga cinco cadenas de caracteres, con uno, dos, tres
#cuatro, tres, cuantro y cinco asteriscos
print("Ejericio 47")
print("-----------\n\n")

lista = []
for asterisco in range(1, 6):
    lista.append("*" * asterisco)
print(lista)

print()

listaComprension = ["*" * n for n in range(1, 6)] #Se lee: n por asterisco, tal que por cada n en el rango [1, 6>
print(listaComprension)