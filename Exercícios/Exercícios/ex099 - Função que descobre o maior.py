from time import sleep


def maior(*valor):
    maior = 0
    print('-=-' * 13)
    print('Analisando os valores passados:',end=' ')
    for c, v in enumerate(valor):
        if c == 1:
            maior = v
        else:
            if v > maior:
                maior = v
        sleep(0.5)
        print(v, end=' ')
    sleep(0.5)
    print(f'\nForam informados {len(valor)} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


# Programa principal
maior(2, 9, 7, 5, 4, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
