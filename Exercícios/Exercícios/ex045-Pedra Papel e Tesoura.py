import random
import time

lista = ['Pedra', 'Papel', 'Tesoura']
computador = random.randint(0,2)

print('''SUAS OPÇÕES:
0-PEDRA
1-PAPEL
2-TESOURA''')
jogador = int(input('QUAL A SUA JOGADA: '))
print('-=-'*12)
print('Computador jogou {}\nJogador jogou {} '.format(lista[computador],lista[jogador]))
print('-=-'*12)

print('\033[32mJO\033[m')
time.sleep(1)
print('\033[33mKEN\033[m')
time.sleep(1)
print('\033[34mPÔ!\033[m')
time.sleep(1)

if computador == 0: #COMPUTADOR JOGOU PEDRA
    if jogador ==0:
        print('EMPATOU')
    elif jogador == 1:
        print('\033[31mJOGADOR GANHOU\033[m')
    elif jogador == 2:
        print('\033[31mJOGADOR PERDEU\033[m')

if computador == 1: #COMPUTADOR JOGOU PAPEL
    if jogador ==1:
        print('\033[31mEMPATOU\033[m')
    elif jogador == 2:
        print('\033[31mJOGADOR GANHOU\033[m')
    elif jogador == 0:
        print('\033[31mJOGADOR PERDEU\033[m')


if computador == 2:#COMPUTADOR JOGOU TESOURA
    if jogador ==2:
        print('\033[31mEMPATOU\033[m')
    elif jogador == 0:
        print('\033[31mJOGADOR GANHOU\033[m')
    elif jogador == 1:
        print('\033[31mJOGADOR PERDEU\033[m')
else:
    print('OPÇÃO INVALIDA')