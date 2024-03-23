#Muestra por pantalla todos los números primos entre 2 y 100, ambos incluidos.
print("Ejercicio 13")
print("------------\n")

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

for i in range(2, 101):
    if es_primo(i):
        print(i)



    
    
