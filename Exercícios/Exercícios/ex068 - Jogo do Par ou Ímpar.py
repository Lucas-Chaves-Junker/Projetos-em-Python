from random import randint

computador = randint(0, 10)
print('===' * 10)
print('VAMOS JOGAR PAR OU ÌMPAR')
print('===' * 10)
vencer = soma = 0
while True:
    jogador = int(input('Diga um valor: '))
    soma = jogador + computador

    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
    print('---' * 10)
    print(f'Você jogou {jogador} e o computador jogou {computador} total de {soma} ', end='')
    print('DEU PAR' if soma % 2 == 0 else 'DEU ÍMPAR')
    print('---' * 10)

    if tipo == 'P':
        if soma % 2 == 0:
            print('Você VENCEU!')
            vencer += 1
            print('-=-' * 10)
        else:
            print('Você PERDEU! ')
            break

    elif tipo == 'I':
        if soma % 2 == 1:
            print('Você VENCEU!')
            vencer += 1
            print('-=-' * 10)
        else:
            print('Você PERDEU! ')
            print('-=-' * 10)
            break
    print('Vamos jogar novamente...')
print(f'Game Over. Você venceu {vencer} vezes')
