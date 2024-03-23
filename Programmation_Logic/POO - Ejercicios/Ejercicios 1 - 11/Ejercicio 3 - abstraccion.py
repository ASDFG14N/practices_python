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
##########################################################################
mi_personaje = Personaje("Inuyasha", 10, 1, 5, 10)
mi_enemigo = Personaje("Seshomaru", 9, 5, 4, 10)
print("»El nombre del jugador es: ",mi_personaje.nombre)
print("»La fuerza del jugador es: ",mi_personaje.fuerza)
print("»La inteligencia del jugador es", mi_personaje.inteligencia)
print("Mostramos los atributos del personaje antes de subir de nivel")
mi_personaje.atributos()
print("Mostramos los atributos despues de subir de nivel al personaje")
mi_personaje.subir_nivel(1, 2, 0)
mi_personaje.atributos()
print("Comprobamos si el personaje esta vivo")
print(mi_personaje.esta_vivo())
print("Mi personaje tiene una vida de", mi_personaje.vida)
print("Comprobamos la vida del personaje")
print(mi_personaje.morir())
print("Compromabos el daño que se realiza a Inuyasha")
print(f"El daño a {mi_personaje.nombre} es de {mi_personaje.daño(mi_enemigo)}")
print("Veamos el ataque de nuestro personaje")
mi_personaje.atacar(mi_enemigo)
print("¿Los atributos de mi enemigo tambien cambiaron?")
mi_enemigo.atributos()