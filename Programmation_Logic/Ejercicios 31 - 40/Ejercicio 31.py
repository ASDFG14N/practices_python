#Creamos la funcion factorial
def factorial(y):
    factorial = 1
    for i in range(1, y+1):
        factorial = factorial * i
    return factorial
def epowx(n, x):
    epowx = 0
    n1 = 0
    while n1 <= n:
        epowx = epowx + (pow(x, n1)/factorial(n1))
        n1 = n1 + 1
    return epowx
print(epowx(20, 3))
