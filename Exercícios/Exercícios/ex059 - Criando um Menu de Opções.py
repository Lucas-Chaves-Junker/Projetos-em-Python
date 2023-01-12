from time import sleep
soma = 0
produto = 0
novos = 0
c = 0
num1 = int(input('Digite o 1º número: '))
num2 = int(input('Digite o 2º número: '))
while c == 0:

    print('''
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
    menu = int(input('>>>>>>> Qual operação voce deseja realizar: '))

    # SOMA
    if menu == 1:
        soma = num1 + num2
        print('A soma entre {} e {} é {} '.format(num1,num2,soma))

    # MULTIPLICARÇÃO
    elif menu == 2:
        produto = num1 * num2
        print('A multiplicação entre {} e {} é {} '.format(num1,num2,produto))

    # MAIOR ENTRE OS NUMEROS
    elif menu == 3:
        if num1 > num2:
            print('{} é maior que {}'.format(num1, num2))
        elif num1 == num2:
            print('{} é igual a {}'.format(num1,num2))
        else:
            print('{} é menor que {}'.format(num1, num2))
    # REPETIR ENTRADA
    elif menu == 4:
        c = 0
        print('Digite novos numeros')
        num1 = int(input('Digite o 1º número: '))
        num2 = int(input('Digite o 2º número: '))

    # FIM DO PROGRAMA
    elif menu == 5:
        c = 1
    else:
        print('Opção invalida. Tente novamente')
    print('=-='*10)
    sleep(2)
print('Fim do programa! Volte sempre')
