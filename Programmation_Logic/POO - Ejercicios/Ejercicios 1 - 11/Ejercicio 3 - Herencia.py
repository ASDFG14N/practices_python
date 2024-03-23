class Personaje:
    def __init__(self, nombre: str, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def atributos(self):
        print(self.nombre, ":", sep="")
        print("»Fuerza:", self.fuerza)
        print("»Intelignecia:", self.inteligencia)
        print("»Defensa:", self.defensa)
        print("»Vida:", self.vida)
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa
    def esta_vivo(self):
        return self.vida > 0
    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")
    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa
    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        print("La vida de,", enemigo.nombre, "es", enemigo.vida)

#Vamos a heredar de la clase padre
class Guerrero(Personaje):
    def __init__(self, nombre: str, fuerza, inteligencia, defensa, vida, agujero):
        #Toca heredar los atrubitso de la clase padre
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        #Nuevos atributos para el agujero
        self.agujero = agujero
        #Nuevos metodos para la clase heredada
    def cambiar_arma(self):
        opcion = int(input("Selecciona un arma: (1)Colmillo de acero; daño:10, (2)Colmillo Sagrado; daño:9: "))
        if opcion == 1: self.agujero = 10
        elif opcion == 2 : self.agujero = 9
        else: print("Esa opcion no existe")

            





####################################################################
guerrero = Guerrero("Miroku", 8, 10, 6, 100, 5)
guerrero.atributos()
print(guerrero.agujero)
guerrero.cambiar_arma()
guerrero.atributos()
print(guerrero.agujero)
guerrero.atributos()