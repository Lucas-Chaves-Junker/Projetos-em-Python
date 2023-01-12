num = int(input('Verificar números primos: '))
mult = 0
for cont in range(1, num + 1):
    if num % cont == 0:
        print('\033[31m', end=' ')
        mult += 1
    else:
        print('\033[m', end=' ')
    print('{}\033[m '.format(cont), end=' ')
print('\nO número {} foi divísivel {} vezes'.format(num,mult))

if mult == 2:
    print('E por isso ele É PRIMO!')

else:
    print('E por isso ele NÃO É PRIMO!')
