from random import randint
from time import sleep

numeros = []


def sorteia(lista):
    print(f'Sorteando 5 valores da lista: ', end=' ')
    for c in range(0, 5):
        n = randint(1, 10)
        numeros.append(n)
        print(f'{n}', end=' ', flush=True)
        sleep(0.5)
    print('PRONTO!')


def somapar(numeros):
    soma = 0
    for v in numeros:
        if v % 2 == 0:
            soma += v
    print(f'somando os valores pares de {numeros}, temos {soma}')


numeros = list()
sorteia(numeros)
somapar(numeros)
