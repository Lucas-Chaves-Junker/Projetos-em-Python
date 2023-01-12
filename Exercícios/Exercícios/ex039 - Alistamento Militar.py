import datetime
atual = datetime.date.today().year

nasc = int(input('Informe o seu ano de nascimento: '))
sexo = str(input('Informe o sexo [F] ou [M] : ')).upper()
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))

#verifica o sexo
if sexo == 'M':
    #verifica a idade
    if idade < 18 :
        saldo = 18 - idade
        ano = atual + saldo
        print('\nAinda faltam {} anos para o alistamento'.format(saldo))
        print('Seu alistamento sera em {}'.format(ano))

    elif idade == 18:
        print('\nVocê tem que se alistar IMEDIATAMENTE!')

    elif idade > 18:
        saldo = idade - 18
        ano =atual - saldo
        print('\nVocê já deveria ter se alistado há {} anos.'.format(saldo))
        print('Você deveria ter se alistado em {}.'.format(ano))
else:
    print('Mulheres não precisam se alistar para o exercito no Brasil')

