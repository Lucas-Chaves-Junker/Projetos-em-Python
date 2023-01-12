contpar = 0
num = (int(input('Digite o Primeiro número: ')),
       int(input('Digite o segundo número:')),
       int(input('Digite o terceiro número:')),
       int(input('Digite o quarto número:')))

print('Você digitou os valores: {}'.format(num))
print(f'o valor 9 apareceu {num.count(9)} Vez.')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3) + 1}° posição.')
else:
    print('O valor 3 nao foi digitado em nenhuma posição.')
    print(f'Os valores pares digitados foram: ', end=' ')

for c in num:
    if c %2 == 0:
        print(c, end=' ')
