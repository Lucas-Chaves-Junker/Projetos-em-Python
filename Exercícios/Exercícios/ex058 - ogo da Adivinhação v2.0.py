from random import randint

computador = randint(0, 10)
c = 4
palpites = 0

print('--=--' * 12)
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10. tente adivinhar... ')
print('--=--' * 12)

while c != 0:
    jogador = int(input('Em que número eu pensei?'))
    palpites += 1
    if jogador == computador:
        print('PARABÉNS! VOCÊ CONSEGUIU ME VENCER APOS {} TENTATIVAS!'.format(palpites))
        c = 0
    else:
        if jogador > computador:
            print('Menos... Tente novamente')
        if jogador < computador:
            print('Mais... Tente novamente')
