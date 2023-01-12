num = int(input('Digite um número:'))
par = num % 2
if par == 0:
    print('O numero {} é par'.format(num))
else:
    print('O número {} é impar'.format(num))