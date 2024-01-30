# Edad y precision
# Calcular tu edad con la mayor precisión posible y cuantos
# segundos faltan para tu cumpleaños. Utilizando un módulo llamado fechas.py.

from datetime import datetime

dia_nacimiento = int(input("Ingrese el día de su cumpleaños: "))
mes_nacimiento = int(input("Ingrese el mes de su cumpleañor: "))
año_nacimiento = int(input("Ingrese el año de su cumpleaños: "))

fecha_hoy = datetime.now()
fecha_nacimiento = datetime(año_nacimiento, mes_nacimiento, dia_nacimiento)

edad = 