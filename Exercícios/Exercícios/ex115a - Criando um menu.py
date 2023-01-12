def menu(msg):
    print('-' * 30)
    print('MENU PRINCIPAL'.center(30))
    print('-' * 30)
    print('1 - \033[34mVer pessoas cadastradas\033[m ')
    print('2 - \033[34mCadastrar novas pessoas\033[m ')
    print('3 - \033[34mSair do sistemas\033[m ')
    print('-' * 30)


def txt(msg):
    print('-' * 30)
    print(f'Opção {num}'.center(30))
    print('-' * 30)


menu('a')
while True:
    try:
        num = int(input('\033[33mSua opção:\033[m '))
        if num == 1:
            txt('a')
        elif num == 2:
            txt('a')
        elif num == 3:
            print('\033[31mVolte sempre! muito obrigado!\033[m')
            break
        else:
            print('\033[31mERRO: digite uma opção valida\033[m')
            menu('a')
    except ValueError:
        print('\033[31mERRO: Digite um número inteiro válido\033[m')

