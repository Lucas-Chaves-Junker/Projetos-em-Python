fatorial = 1
num = int(input('Digite um número para calcular seu fatorial: '))

# while para impedir que o usúario digite um número negativo
while num < 0:
    if num < 0:
        print('Impossível calcular o fatorial de um número negativo.')
        num = int(input('Digite novamente um número positivo: '))
        print('-=-'*10)
print('Calculando {}! = '.format(num), end='')

# while para realizar o fatorial do numero
while num > 0:
    print(' {} '.format(num), end='')
    print(' X ' if num > 1 else '= ', end='')
    fatorial *= num
    num -= 1
print('{}'.format(fatorial))
