import datetime

data_atual = datetime.date.today().year
nasc = int(input('Informa a data de nascimento do atleta: '))
idade = datetime.date.today().year - nasc

print('Em {} o atleta tem {} anos de idade '.format(data_atual, idade))

if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SENIOR')
elif idade > 25:
    print('Classificação: MASTER')
