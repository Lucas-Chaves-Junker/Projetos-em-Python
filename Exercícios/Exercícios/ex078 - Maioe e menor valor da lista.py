num = []
maior = menor = 0
for c in range(0, 5):
    num.append(int(input(f'Digite o {c} numero: ')))
    if c == 0:
        menor = maior = num[c]
    else:
        if menor > num[c]:
            menor = num[c]
        elif maior < num[c]:
            maior = num[c]

print(f'Você digitou os valores{num}')

print(f'O maior valor é {maior} nas posições: ', end='')
for c, loc in enumerate(num):
    if loc == maior:
        print(c, end=' ')

print(f'\nO menor valor é {menor} nas posições: ', end='')
for c, loc in enumerate(num):
    if loc == menor:
        print(f'{c}', end=' ')
