import math
print("Combinatoria")
print("------------\n\n")
#factorial de un numero
#Para calcular el factorial de un numero entero positivo, usamos el metodo factorial()
print(math.factorial(10))

#Numero combiantorio (n k) = (n!) / (k!*(n-k)!), podemos usar el metodo .comb() 
def chose(n, k):
    if (n >= k and k >= 0):
        return math.factorial(n) / (math.factorial(k) * math.factorial(n-k))
    else:
        return "No se puede calcular el numero factorial indicado"
print(chose(10, 2))