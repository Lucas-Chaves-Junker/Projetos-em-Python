print('\033[0;34mCONVERSOR DE BASE\033[m')

num = int(input('Digite um número inteiro:'))
print('Escolha uma das bases de conversão!')

print('\033[0;33m===\033[m' * 12)
print('1-Converter para binário:'
      '\n2-Converter para octal:'
      '\n3-Converter para hexadecimal:')
print('\033[0;33m===\033[m' * 12)
base = int(input('Sua oção:'))
if base == 1:
    print('{} convertido para BINÁRIO É {}:'.format(num, bin(num)[2:]))
elif base == 2:
    print('{} convertido para OCTAL É {}:'.format(num, oct(num)[2:]))
elif base == 3:
    print('{} convertido para HEXADECIMAL É {}:'.format(num, hex(num)[2:]))
else:
    print('Opção invalida!')
