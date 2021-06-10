import os
os.system('cls')
Periodo = int(input('Escriba una cantidad de segundos que quiera descomponer:  '))
Horas = Periodo // 3600
Dias = Horas // 24
FraccDias = ((Periodo/3600)-Horas)
Hscompletas = int(FraccDias*24)
MinMenores = ((FraccDias*24)-Hscompletas)
Minutos = int(MinMenores*60)
print(Minutos)
Deciminutos = ((MinMenores*60)-Minutos)
print(Deciminutos)
Segundos = int(Deciminutos*60)
print('Forman ', Dias, ' días, ', Hscompletas, ' horas, ', Minutos, ' minutos, y ', Segundos,'Segundos' )

Segundos = int(input('Escriba una cantidad de segundos que quiera descomponer:  '))
Days = Segundos // (24*60*60)
Segundos = Segundos % (24*60*60)
Horas = Segundos //(60*60)
Segundos = Segundos % (60*60)
Minutos = Segundos //60
Segundos = Segundos % 60
print('Forman ', Days, ' días, ', Horas, ' horas, ', Minutos, ' minutos, y ', Segundos,'Segundos' )
print('Dias: {} - Horas {} - Minutos {} - Segundos {}'.format(Days, Horas, Minutos, Segundos))
