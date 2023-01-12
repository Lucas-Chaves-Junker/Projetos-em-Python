def escreva(*txt):
    print('~' * (len(*txt) + 4))
    for c in txt:
        print(f'  {c}')
    print('~' * (len(*txt) + 4))


while True:
    escreva(str(input('Escreva uma frase: ')))
    while True:
        resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
        if resp in 'NS':
            break
    if resp == 'N':
        break
