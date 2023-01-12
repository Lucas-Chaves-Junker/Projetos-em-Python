pessoas = []
temp = []
maior = menor = 0
while True:
    temp.append(str(input('Digite seu nome: ')))
    temp.append(int(input('Digite seu peso: ')))

    if len(pessoas) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]

    pessoas.append(temp[:])
    temp.clear()

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'O maior peso foi de {maior:.2f}Kg peso de', end=' ')
for i in pessoas:
    if maior == i[1]:
        print(i[0], end=' ')
print(f'\nO menor peso foi de {menor:.2f}Kg peso de', end=' ')
for i in pessoas:
    if menor == i[1]:
        print(i[0], end=' ')
print(f'\nVocê cadastrou {len(pessoas)} pessoas')
