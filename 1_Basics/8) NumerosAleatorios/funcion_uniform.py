#Trabaja con numeros reales 
#Sintaxis ==> random.uniform(a, b)
#Devuelve un numero real aleatorio entre lso numeros reales a y b, donde no es necesario que a < b. Tanto a como b 
# estan incluidos pero por motivos de redondeo no es seguro que b esté de forma efectiva. #
import random
print("Funcion uniform()")
print("-----------------\n")

print(random.uniform(float(input("Introduce un numero real: ")), float(input("Introduce otro numero real: "))))
