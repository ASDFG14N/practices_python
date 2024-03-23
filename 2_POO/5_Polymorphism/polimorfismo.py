class Spain():
    def capital(self):
        print("Madrid es la capital de España")
    def lenguaje(self):
        print("En españa se habla el castellano")
class Portugal():
    def capital(self):
        print("La capital de portugal es Lisboa")
    def lenguaje(self):
        print("En portugal se habla el portugues")
#vemos que tienen metodo que se llaman igual
españa = Spain()
portugal = Portugal()
for pais in (españa, portugal):
    pais.capital()
    pais.lenguaje()
    print("")