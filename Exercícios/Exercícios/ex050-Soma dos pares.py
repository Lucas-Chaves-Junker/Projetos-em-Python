soma = 0
i = 0
for cont in range(1,7,+1):
    num = int(input('Digite o {}º numero: '.format(cont)))
    if num % 2 == 0:
        soma += num
        i += 1
print('Você informou {} numero(s) pares e a soma desses números é {}'.format(i,soma))