from collections import defaultdict

#Creo un elemento para un key que no existia
diccionario = defaultdict(lambda: "nada")
diccionario["uno"] = "verde"
print(diccionario["dos"])
print(diccionario)