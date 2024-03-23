import math
#Maximo comun divisor y minimo comun multiplo
#============================================

#Para calcular el maximo comun divisor de dos numeros, usamos .gcd()
print(math.gcd(16, 8))
print(math.gcd(27, 16)) #son primos entre si

#Para calcular el minimo comun multiplo de dos numeros, usamos .lcm()
def lcm2(a, b):
    return math.fabs(a*b) // math.gcd(a, b)
print(lcm2(16, 8))