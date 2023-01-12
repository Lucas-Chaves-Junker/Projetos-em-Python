def fat(num=0, show=False):
    """
    -> Função que calcula o fatorial de um número
    :param num: O número a ser calculado
    :param show: (Opicional) Mostra ou não a conta.
    :return: O valor do fatorial de um número n.
    """
    resp = 1
    for c in range(num, 0, -1):
        if show:
            print(f'{c}', end=' ')
            if c > 1:
                print('X', end=' ')
            else:
                print('=', end=' ')

        resp *= c
    return resp


n = int(input('escreva um número:'))
print(fat(n, show=False))
