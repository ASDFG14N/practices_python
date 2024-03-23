#Este metodo permite concatenar dos o mas listas y a sus vez permite agrgar varios elememtos a una lista.
#Sistaxis:
#nombre_lista.extend(objetoIterable)
print("Metodo extend()")
print("---------------\n")
invitados = ["Carolina", "Juan", "Gerardo"]
amigos = ["Luis", "Ana"]
print(f"Lista invitados: {invitados} \nLista amigos: {amigos}")
invitados.extend(amigos)
print(f"Lista invitados con el metodo extend: {invitados}")

numeros = [10, 20]
print(f"\nLista números: {numeros}")
numeros.extend(range(30, 100, 10))
print(f"Lista números: {numeros}")