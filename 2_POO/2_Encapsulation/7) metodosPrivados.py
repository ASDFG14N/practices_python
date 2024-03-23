#De la misma manera que podemos ddefinir campos provados podemos definir metodos privados. 
# Un método privado en Python es un método que no se puede acceder desde fuera de la clase y solo 
# puede ser utilizado dentro de la clase. Estos métodos no son accesibles directamente desde el objeto, 
# sino que solo pueden ser llamados a través de otros métodos de la clase
# El formato para indicarlo es colocando dos guienes bajos seguidos del nombre de metodo.
#                       ==> def__nombre_del_metodo(self, [posibles_parametros_formales])
#y en llamada:
#                       ==> self.__nombre_del_metodo(posibles_argumentos)

#Ejemplo de un metodo privado:
class ClaseEjemplo:
    def __init__(self): #Metodo costructor
        self.public_field = "Campo público" # este es un campo público accesible desde afuera de la clase
        self.__private_field = "Campo privado" # este es un campo privado que no puede ser accedido desde 
                                                #afuera de la clase
    
    def public_method(self): #Este es un metodo publico
        return "Este es un método público"
    
    def __private_method(self): # este es un método privado que no puede ser llamado desde afuera de la clase
        return "Este es un método privado"
    
    def acceso_privado(self):
        return self.__private_field + " " + self.__private_method() # aquí dentro de la clase, 
                                                            #podemos acceder a los métodos y campos privados

objeto = ClaseEjemplo() #Creamos una instacia de la claseEjemplo

# imprime: "Campo público"
print(objeto.public_field) 

# genera un error, ya que no podemos acceder al campo privado desde afuera de la clase
print(objeto.__private_field) 

# imprime: "Este es un método público"
print(objeto.public_method()) 

# genera un error, ya que no podemos llamar al método privado desde afuera de la clase
print(objeto.__private_method()) 

# imprime: "Campo privado Este es un método privado"
print(objeto.acceso_privado()) 
