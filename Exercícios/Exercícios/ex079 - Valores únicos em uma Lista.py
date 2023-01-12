numeros = list()

while True:
    n = int(input('Digite um valor: '))

    if n not in numeros:
        numeros.append(n)
        print('Salvo com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja coninuar? [S/N] ')).upper().strip()[0]
    if resp in 'N':
        break
numeros.sort()
print('=-='*13)
print(f'Você digitou valores {numeros}')
