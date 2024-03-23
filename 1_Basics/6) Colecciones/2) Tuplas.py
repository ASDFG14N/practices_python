#Son muy parecidas a las listas, ademas comparten varias funciones y mentodos integrados, sin embargo,
#Su diferencia principal es que son IMNUTABLES, es decir no se pueden modificar
#Tambien son mas eficaces para operar con la informacion.
# Sintaxis:
#tuple(objetos) #Los objetos pueden ser de cualquier tipo
print("Tuplas")
print("------\n")

tuplaVacia = ()
print(tuplaVacia) 

tupla = (4, "Hola", 6.78, 4, True, False)
print(tupla)
#Van a haber metodos compatibles con las listas pero no con las tuplas, entonces ¿para que sirven las tuplas?
#gracias estas estructuras se puede buscar algun elemento, por ejemplo en un bucle.
print()
print(4 in tupla)
print(tupla.index(6.78))
print(tupla.count(4))
print(f"Cuantos elementos tiene la tupla?: {len(tupla)}")
print()

#Podemos tranformar listas a tuplas y tuplas a listas
print("\nTupla trasformada a Lista")
print(f"{list(tupla)} \n")
print("\nLista transformada a Tupla")
lista = [1,2,2,5,47,6]
print(lista)
print(tuple(lista))
print()

#Operadores sobre tuplas (: , +, *, in, noy in, <, <=, >, >=, ==, !=)
print("Operadores sobre listas")
t = (12,5,2)
t2 = (3, 7, 9, 10)
print(t[1:2]) #Operador de troceado
print(t2[1:3])
print(t+t2) #une secuencialmente dos tuplas en una
print(t2*3) #Repite secuencialmente un numero entero de veces la tupla
print(2 in t2) #Indica si el elemento 10 esta en la tupla t2
print(12 in t)

#funciones aplicadas tuplas
#son las siguintes len(), max(), min(), sum()

#metodos de la clase tuple
#son solo dos count(), intex()



print()
#Tuplas bidimencionales:
tupla_bidimensional = ((1, 2), (3, 4), (5, 6))
# se puede acceder a los elementos de la tupla bidimensional utilizando índices dobles,
# como en tupla_bidimensional[1][0] para acceder al elemento 3 en la segunda fila y primera columna.
print(tupla_bidimensional[1][0])










