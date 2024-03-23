#genera secuencias de numeros que no se puden modificar, estas secuancias se generan detro de un rango
# previamente establecido por el programador. 
#generalmente se utiliza como objeto iterable dentro de la intruccion for

#sintaxis:
#range(stop) ==> numerop hasta el cual se generan los numeros y no sera parte de la secuencia(un argumento)
#range(start, stop) ==> (dos armunetos)
#range(start, stop, step) ==> step incica el incremento o decremento de la succecion numerica entre un numero
#y el siguiente

numeros = range(10) #[0,1,2,3,4,5,6,7,8,9]
print(numeros[5])

numeros2 = range(3, 10) #[3,4,5,6,7,8,9]
print(numeros2[4])

numeros3 = range(5, 60, 5) #[5,10,15,20,25,30,35,40,45,50,55] 
print(numeros3[10])
#cuando se crea un rango siempre empieza a contar desde la pocicion cero
print("-------------------------------------------------------------------------------")
#for con range
for indice in range(1, 5):
    print(indice)
print("Fin del ejemplo")
print("-------------------------------------------------------------------------------")
numero = int(input("Introduce el numero que deseas ver tabla de multiplicar: "))
for i in range(11):
    print(f"{numero} x {i} = {numero*i}")