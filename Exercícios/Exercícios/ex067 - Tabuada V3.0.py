while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num <= 0:
        break
    print('===' * 12)
    for cont in range(1,11):
        print(f'{num} X {cont:2} = {num*cont}')
    print('===' * 10)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
