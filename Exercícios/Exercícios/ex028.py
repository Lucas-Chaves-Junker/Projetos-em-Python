from random import randint
from time import sleep

computador = randint(0, 5)
print('--=--' * 12)
print('Vou pensar em um número entre 0 e 5. tente adivinhar... ')
print('--=--' * 12)
jogador = int(input('Em que número eu pensei?'))
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('PARABÉNS! VOCÊ CONSEGUIU ME VENCER!')
else:
    print('GANHEI! EU PENSEI NO NÚMERO {} E NÂO NO {}! '.format(computador, jogador))
