class Coche: #Definimos la clase Coche
    def __init__(self, marca, modelo): #Metodo constructor __init__, posee dos parametros, ambos proivados
        self.__marca = marca
        self.__modelo = modelo
        
    def get_marca(self):
        return self.__marca
    
    def get_modelo(self):
        return self.__modelo

coche = Coche("Toyota", "Camry")
print(coche.get_marca()) # Imprime: Toyota
print(coche.get_modelo()) # Imprime: Camry
print(coche.__marca) # Produce un error, ya que __marca es un campo privado
