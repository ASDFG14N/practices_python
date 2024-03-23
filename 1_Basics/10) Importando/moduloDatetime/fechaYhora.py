import datetime
#podemos trabajar con horas
miHora = datetime.time(15, 22)
print(miHora)
#fechas
miDia = datetime.date(2021, 10, 8)
print(miDia)
print(miDia.year)
print(miDia.today())

print()

from datetime import date
nacimiento = date(1995, 3, 8)
muerte = date(2095, 6, 9)
vida = muerte - nacimiento
print(vida) #ouput dias que estuvo viva la persona

print()

from datetime import datetime
despierto = datetime(2022, 10, 5, 7, 30)
duerme = datetime(2022, 10, 5, 23, 45)
vigilia = duerme - despierto
print(vigilia) #sale en horas y minutos
print(vigilia.seconds) #solo en segundos

