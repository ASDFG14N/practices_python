print("Funcion filter")
print("--------------")

#usando una lambda
nums = [49, 57, 62, 147, 2101, 22]
lista = list(filter(lambda x: (x % 7 == 0), nums))
print(lista)

#usando una funcion
def la_tercera_letra_es_s(palabra):
    return palabra[2] == "s"
print(la_tercera_letra_es_s("assiris"))

#combinando la funcion creada mas la funcion filter
palabras = ["Castaña", "Astronomia", "masa", "boligrafo", "tostada"]
lista2 = list(filter(la_tercera_letra_es_s, palabras))
print(lista2)