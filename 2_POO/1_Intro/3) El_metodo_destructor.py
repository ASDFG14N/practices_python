class Book():
    """
    Clase para trabajar con libros
    """
    def __init__(self, titulo, autor = "", electronico = False): #El constructor es llamado cuando se crea un objeto
        #de la clase.
        self.titulo = titulo
        self.autor = autor
        self.es_electronico = electronico
    def __del__(self):
        print("El objeto acaba de ser eliminado")