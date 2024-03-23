#Crea un método estático respirar() para la clase Mascota. 
#Cuando se llame, debe imprimir en pantalla "Inhalar... Exhalar"
class Mascota():
    @staticmethod
    def respirar():
        print("Inhalar... Exalar")
print(Mascota.respirar())
#Crea un método de clase revivir() que actúa sobre el atributo 
#de clase vivo de la clase Jugador, estableciéndolo en True cada vez que es invocado. 
#El valor predeterminado del atributo vivo, debe ser False.
class Jugador():
    vivo = True
    @classmethod
    def revivir(cls):
        cls.vivo = False
