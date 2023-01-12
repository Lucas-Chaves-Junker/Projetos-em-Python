from random import randint
from time import sleep

jogos = []
lista = []
cont = 0
tot = 1

print('-=' * 20)
print(f'{"          JOGA NA MEGA SENA":^20}')
print('-=' * 20)

quant = int(input('Quantos jogos você quer que eu faça? '))
while tot <= quant:
    cont = 0
    while True:
        rendt = randint(1, 60)
        # verificando números repetidos
        if rendt not in lista:
            lista.append(rendt)
            cont += 1
        if cont == 6:
            break

    jogos.append(lista[:])
    lista.clear()
    tot += 1

print('\n', '-=' * 3, f'SORTEANDO {quant} JOGOS', '=-' * 3)
for c, t in enumerate(jogos):
    sleep(1)
    print(f'Jogo{c + 1}°: {jogos[c]}', end=' ')
    print()
