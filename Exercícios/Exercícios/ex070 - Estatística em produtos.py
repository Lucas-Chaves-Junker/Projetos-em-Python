total = 0
totmil = 0
menor = 0
cont = 0
barato = ''
while True:
    produto = str(input('O nome do produto: ')).strip().upper()
    preco = float(input('Informe o preço do produto: R$'))
    cont += 1
    total += preco
    if preco > 1000:  # produto mais caro
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]')).strip().upper()[0]

    if resp == 'N':  # condição de parada do laço principal
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total:.2f} ')
print(f'Temos {totmil} produtos que custam mais de R$1000.00 ')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
