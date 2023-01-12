flag = 'S'
cont = media = maior = menor = soma = 0

while flag in 'S':
    num = int(input('Digite um número: '))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    flag = str(input('Quer continuar? [S/N]')).upper().strip()[0]
media = soma / cont
print('Você digitou {} e a media é {:.2f}.'.format(cont, media))
print('O maior numero é {} e o menor numero é {} '.format(maior, menor))
