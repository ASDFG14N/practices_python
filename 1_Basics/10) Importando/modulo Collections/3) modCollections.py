from collections import namedtuple

persona = namedtuple("Persona", ["nombre", "altura", "peso"])
ariel = persona("Gian", "1,65", "50")
print(ariel.altura)