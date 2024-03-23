from collections import Counter
#Podemos contas las letras que se repiten
c = Counter('abcdeabcdabcaba')
print(c) #cuenta los elementos de un string

print()

#Podemos contar los numeros que se repiten
numeros = [1,1,8,2,5,1,9,4,8,4,7,3,5,6,9,8,8,] #cuenta los elementos de una lista
print(Counter(numeros))

print()

#podemos contar las palabras que se repiten en una frase
frase = "al pan pan y al vino vino"
print(Counter(frase.split()))

print()

#Podemos contar los elementos unicos de una lista

serie = Counter([1,1,1,1,1,1,2,2,2,2,3,3,3,3,3,4,4,4])
print(list(serie))