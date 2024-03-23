cadena = "\tHola Ernesto\n" #(\t: tabulacion ==> consite en 4 espacios a la derecha)
print(cadena) #imprime la cadena 

#######################################################################################

cadena = cadena.strip() #Al no epecificar al metodo strip en los parentesis lo que hara sera borra los epsacios 
                        #en blanco(4 a la derecha y un salto de linea)
print(cadena)

#######################################################################################

cadena2 = "\tHola Gian\n"
print(cadena2)
cadena2 = cadena2.strip(" i \t\nHn ") #busca cadenas de carateres al inicio o final de la cadena de texto
                                       #si no la escuentra no le hace nada a la misma, recordar que los refiva uno por uno
                                       #los que esteen entre parentesis, ejeplo, al inicio revisa si hay una "H" mayuscula
                                       #al inicio o final de la variable, como no hay hace lo mismo con los siguientes
                                       #caracteres detro del parentesis, uno por uno. Cuando encuentra uno, vuelve al 
                                       #inicio y no brinca a la siguiente letra
print(cadena2)