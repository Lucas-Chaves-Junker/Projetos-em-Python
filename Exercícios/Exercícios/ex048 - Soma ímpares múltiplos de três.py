soma = 0
i = 0
for cont in range(1, 501, +2):
    if cont % 3 == 0:
        soma +=cont
        i = i+1
print('A soma dos {} multiplos de 3 é {}' .format(i,soma))
