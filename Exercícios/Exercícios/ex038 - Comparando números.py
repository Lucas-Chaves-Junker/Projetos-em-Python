num1 = int(input('Dinite o primeiro número inteiro: '))
num2 = int(input(' Digite o segundo número inteiro: '))

if num1 > num2:
    print('O \033[31mPRIMEIRO\033[m valor é maior.')
elif num2 > num1:
    print('O \033[31mSEGUNDO\033[m valor é maior.')
else:
    print('Não exite valor maior. Os dois são \033[31mIGUAIS\033[m . ')
