#Escriba una aplicación que reciba tres enteros del usuario y muestre la suma,
#promedio, producto, menor y mayor de esos números. Utilice las técnicas que se muestran en la figura 2.15 
#[nota: el cálculo del promedio en este ejercicio debe dar como resultado una representación entera del promedio. 
#Por lo tanto, si la suma de los valores es 7, el promedio debe ser 2, no 2.3333...].
print("Ejercico #3")
print("-----------\n")

def Operaciones(x, y, z):
    suma = x + y + z
    producto = x*y*z
    promedio = (suma) / 3
    print("La suma es:", suma)
    print("El producto es:", producto)
    print("El promedio es:", promedio)
def Mayor_Menor(x, y, z):
    if (x > y) and (y > z):
        print("El numero mayor es", x, "y el menor es:", z)

numUno = int(input("Introduce el primer numero: "))
numDos = int(input("Introduce el segundo numero: "))
numTres = int(input("Introduce el tercer numero: "))
Operaciones(numUno, numDos, numTres)
Mayor_Menor(numUno, numDos, numTres)
