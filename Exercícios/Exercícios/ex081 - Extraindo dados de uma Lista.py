num = []
while True:
    n = num.append(int(input('Digite um valor: ')))

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('-=-'*15)
print(f'Você digitou {len(num)} elementos.')
num.sort(reverse=True)
print(f'Os valores em decrescente são {num}')
if 5 in num:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
