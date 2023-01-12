import datetime
from datetime import date

dados = {}
dados['Nome'] = str(input('Nome: '))
nasc = int(input('Data de nascimento: '))
dados['Idade'] = datetime.date.today().year - nasc
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))

if dados['ctps'] != 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: R$'))
    dados['Aposentadoria'] = (dados['Idade'] + ((dados['Contratação'] + 35) - datetime.date.today().year))

print('---'*20)
for k, v in dados.items():
    print(f'{k} Tem o valor {v}')
