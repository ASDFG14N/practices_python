import psutil
#Comprobar si dos numeros son amigos.
print("\tEjercicio 35")
print("\t------------\n")
def sumaDivisores (num):
    divisor, sumaDivisor = 0, 0
    for i in range(1, num + 1):
        if num % i == 0:
            divisor = int (num / i)
            sumaDivisor = sumaDivisor + divisor
    return sumaDivisor - num
def numerosAmigos(numUno, numDos):
    sumaDivisorUno = sumaDivisores(numUno)
    sumaDivisorDos = sumaDivisores(numDos)
    if sumaDivisorUno == numDos and sumaDivisorDos == numUno: print("Son numeros amigos")
    else: print("No son numeros amigos :'v")
numerosAmigos(1181, 1210)
numerosAmigos(17296, 18416)
process = psutil.Process()
print(f"Uso de memoria: {process.memory_info().rss / 1024 ** 2:.2f} MB")
