num = 0
soma = 0
tot = 0
num = int(input('Digite um numero [999 para parar]: '))
while num != 999:
    soma += num
    tot += 1
    num = int(input('Digite um numero [999 para parar]: '))
print('Você digitou {} números e a soma entre eles é {}. '.format(tot,soma))
