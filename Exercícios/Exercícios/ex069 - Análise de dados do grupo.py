tot18 = 0
totM = 0
totF = 0

while True:
    print('CADASTRE UMA PESSOA')
    print('---' * 10)
    idade = int(input('digite sua idade:'))

    sexo = ' '
    while sexo not in 'FM':  # estrutura de repetição para obrigar a entrada correta
        sexo = str(input('Digite seu sexo: [F/M]')).strip().upper()[0]
    print('---' * 10)

    # análise das informaçoes
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totM += 1
    if sexo == 'F' and idade < 20:
        totF += 1

    resp = ' '
    while resp not in 'SN':  # estrutura de repetição para obrigar a entrada correta
        resp = str(input('Deseja continuar? [S/N]')).strip().upper()[0]

    if resp == 'N':  # condição de parada do laço
        print('===== FIM DO PROGRAMA ======')
        break
    print('---' * 10)

# saida com as informaçoes formatadas
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totM} homens cadastrados.')
print(f'E temos {totF} mulher com menos de 18 anos.')
