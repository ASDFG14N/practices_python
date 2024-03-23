class Alarma:
    def postergar(self,cantidad_minutos):
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")
alarma = Alarma()
print(alarma.postergar(8))