#Dada una lista, crear otra que contenga solo los numeros pares
datos = [14, 18, 21, 29, 36, 41, 58, 63, 74]
#Primera forma, lista por extencion
listaParesUno = []
for numPar in datos:
    if numPar % 2 == 0:
        listaParesUno.append(numPar)
print(listaParesUno)
#Segunda forma: lista por comprension
listaParesDos = [numPar for numPar in datos if numPar % 2 == 0]
print(listaParesDos)

#Dada la misma lista datos, queremos una nueva lista que tenga solo los numeros pares mayores de 30
listaParesMayores = [numPar for numPar in datos if numPar % 2 == 0 if numPar > 30]
print(listaParesMayores)
