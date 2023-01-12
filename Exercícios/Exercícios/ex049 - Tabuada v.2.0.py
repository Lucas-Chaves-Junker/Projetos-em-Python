num = int(input('Informe um número para ver sua tabuada: '))

for cont in range(0, 11, +1):
    print('{} X {:2} = {} '.format(num, cont, (cont * num)))
