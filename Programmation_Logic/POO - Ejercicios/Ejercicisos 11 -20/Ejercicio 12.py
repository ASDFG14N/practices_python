#Cuentas con tres clases de personajes en un juego, los cuales cuentan con sus métodos de ataque específicos.
#Crea un iterador que logre un ataque conjugado en el siguiente orden: Arquero, Mago, Samurai, 
#llamando al método atacar() de cada uno de los personajes. Deberás crear instancias de cada una de las clases
#anteriores para construir un iterable (una lista llamada personajes) que pueda recorrese en dicho orden.
class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")
class Mago():
    def atacar(self):
        print("Ataque mágico")
class Samurai():
    def atacar(self):
        print("Ataque con katana")
#Instancias
gandalf = Mago()
hawkeye = Arquero()
jack = Samurai()
#funcion atacar
def personajeAtaque(nombrePesonaje):
    nombrePesonaje.atacar()
personajeAtaque(gandalf)
personajeAtaque(hawkeye)
personajeAtaque(jack)

