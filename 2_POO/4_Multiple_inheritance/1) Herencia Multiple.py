# Clase padre Operacion
#1) La clase padre Operacion tiene dos atributos, valor1 y valor2
class Operacion:
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2
    #Estos son los metodos de la clase padre  
    def suma(self):
        return self.valor1 + self.valor2
    
    def resta(self):
        return self.valor1 - self.valor2
    
# Clase hija Multiplicacion heredando de la clase Operacion
#La clase hija Multiplicacion hereda los metodos y atributos de la clase Operacion y agrega un método 
#multiplicacion
class Multiplicacion(Operacion):
    def multiplicacion(self):
        return self.valor1 * self.valor2

# Clase hija Division heredando de la clase Operacion
#La clase hija Division también hereda de la clase Operacion y agrega un método division
class Division(Operacion):
    def division(self):
        return self.valor1 / self.valor2

# Clase hija Potencia heredando de las clases Multiplicacion y Division
class Potencia(Multiplicacion, Division):
    def potencia(self):
        return self.valor1 ** self.valor2

# Creamos un objeto de la clase Potencia
#Al crear un objeto de la clase Potencia, se pueden usar todos los métodos de la clase Operacion, 
# Multiplicacion y Division, así como el método potencia de la clase Potencia.

n = int(input("Introduce el primer valor: "))
j = int(input("Introduce el segundo valor: "))
objeto = Potencia(n,j)

# Mostramos el resultado de las operaciones
print("La suma es: ", objeto.suma()) #usamos el metodo suma de la calse operaciones
print("La resta es: ", objeto.resta())
print("La multiplicación es: ", objeto.multiplicacion())
print("La división es: ", objeto.division())
print("La potencia es: ", objeto.potencia())