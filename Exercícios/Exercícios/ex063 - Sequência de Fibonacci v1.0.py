print('===' * 10)
print('Sequência de Fibonacci')
print('===' * 10)
num = int(input('Quantos termos você quer mostrar? '))
f1 = 0
f2 = 1
print('~~~~' * 10)
print('{} -> {} '.format(f1, f2), end='')
cont = 3
f3 = 0
while cont <= num:
    f3 = f1 + f2
    print('-> {} '.format(f3), end='')
    f1 = f2
    f2 = f3
    cont += 1
print('-> FIM')
print('~~~~'*10)

