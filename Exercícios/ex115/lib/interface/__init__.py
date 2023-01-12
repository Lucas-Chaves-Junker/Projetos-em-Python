def linha(tam=42):
    return '-' * tam


def leia_int(n):
    while True:
        try:
            entrada = int(input(n))

        except (TypeError, ValueError):
            print('\033[31mERRO! Digite um número inteiro valido\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não digitar esse número\033[m')
            return 0
        else:
            return entrada


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    linha()
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    linha()
    opc = leia_int('\033[33mSua opção:\033[m ')
    return opc


