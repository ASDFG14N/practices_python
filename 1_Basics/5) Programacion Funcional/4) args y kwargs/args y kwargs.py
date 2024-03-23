# *args nos almacenara en tuplas 
def args_funtion(*args):
    print(args)

#Cunado colocamos **kwargs nos almacenara en kwargs, que sera la estrucura de datos llamada diccionario
def kargs_funtion(**kwargs):
    print(kwargs)

def funtion(dic):
    print(dic)
    
#Llamado a las funciones
args_funtion(8, 6, 7, 7)
kargs_funtion(Gian = 20, Paola =  25, Elvia =  55)


diccionario = {"Gian": 20, "Paola": 25, "Elvia": 55}
funtion(**diccionario["Gian"])

