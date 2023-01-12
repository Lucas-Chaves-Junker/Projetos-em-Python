def leia_int(n):
    while True:
        try:
            entrada = int(input('Digite um número Inteiro: '))

        except (TypeError, ValueError):
            print('\033[31mERRO! Digite um número inteiro valido\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não digitar esse número\033[m')
            return 0
        else:
            return entrada


def leia_float(f):
    while True:
        try:
            entrada = str(input('Digite um número Real: ')).replace(',', '.')
            entrada = float(entrada)
        except (TypeError, ValueError):
            print('\033[31mERRO! Digite um número Real valido\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não digitar esse número\033[m')
            return 0
        else:
            return entrada


num1 = leia_int('Escreva um número inteiro: ')
num2 = leia_float('Escreva um número flutuante: ')
print(f'O valor Inteiro digitado foi {num1} e o Real foi {num2}')
