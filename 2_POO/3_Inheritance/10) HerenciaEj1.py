class Math: #SuperClase
    def __init__(self, num1, num2): #Constructor que define los atributos
        self.num1 = num1
        self.num2 = num2

class Addition(Math): #Subclase
    def add(self):
        return self.num1 + self.num2

class Subtraction(Math): #Subclase
    def subtract(self):
        return self.num1 - self.num2

math_obj = Addition(10, 20)
print("Suma: ", math_obj.add())

math_obj = Subtraction(30, 15)
print("Resta: ", math_obj.subtract())