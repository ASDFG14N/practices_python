class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def __str__(self):
        return f"{self.nombre} tiene {self.edad} años"

persona = Persona("Messi", 35)
print(str(persona))