#Realizar el Pseudocódigo para sumar 2 matrices.
#Sean 2 matrices A y B ambas bidimensionales, para que se puedan sumar deben poseer el mismo número de filas 
# y columnas, cada elemento de la matriz resultante será la suma de los correspondientes elementos de las 
# matrices A y B.
#C(i , j) = A (i , j) + B (i , j)
#Usando listas
print("\tEjercicio 26")
print("\t------------\n")

A = []
B = []
C = []

print("Ingrese las dimensisones de la matriz")
filas = int(input("Numero de filas de la matriz: "))
columnas = int(input("Numero de columnas de la matriz: "))

for i in range(filas):
    A.append([]) #Agrega una fila vacia a la matriz A
    B.append([]) #Agrega una fila vacia a la matriz B
    C.append([]) #Agrega una fila vacia a la matriz C
    for j in range(columnas):
        A[i].append( int( input("A{}{}: ".format(i+1,j+1))))
        B[i].append( int( input("B{}{}: ".format(i+1,j+1)))) 
        C[i].append( A[i][j] + B[i][j])

print(f"{A} + {B} = {C}") 
