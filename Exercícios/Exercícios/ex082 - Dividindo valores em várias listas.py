num = []
par = []
impar = []

while True:
    n = num.append(int(input('Digite um numero: ')))

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar: [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
for c in num:
    if c % 2 == 0:
        par.append(c)
    elif c % 2 == 1:
        impar.append(c)

print(f'A lista completa é {num}')
print(f'A lista de par é {par}')
print(f'A lista de impar é {impar}')
