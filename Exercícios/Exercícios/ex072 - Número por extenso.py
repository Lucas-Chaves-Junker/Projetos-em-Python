numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis',
           'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
           'catorze', 'Quinze', 'Dezesseis', 'Dezessete',
           'Dezoito', 'Dezenove', 'Vinte')

while True:
    num = int(input('Digite um Número entre 0 e 20: '))

    if 0 <= num <= 20:
        print(f'Você digitou o número {numeros[num]}')
    else:
        print('NÚMERO INVALIDO! Digite um número entre 0 e 20. ')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break

