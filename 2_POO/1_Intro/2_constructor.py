class Book():
    """
    Clase para trabajar con libros
    """
    def __init__(self, titulo, autor = "", electronico = False):
        self.titulo = titulo
        self.autor = autor
        self.es_electronico = electronico


libro_1 = Book("Calculo infinitesimal", "Spivak", True)
print(libro_1.titulo)
print(libro_1.autor)
print(libro_1.es_electronico)
#para acceder a todos los atributos de un ojeto usamos el metodo __dict__
#print(libro_1.__dict__)
#print(libro_1.__doc__)

