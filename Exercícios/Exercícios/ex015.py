dias_aluguel = int(input('Quantos dias o carro foi alugado? '))
km_rodado = float(input('Quantos KM rodados? '))

valor_total = ((dias_aluguel * 60) + (km_rodado * 0.15))

print('O carro que foi alugado por {} dias e percorreu {}Km custa R${:.2f}'.format(dias_aluguel, km_rodado, valor_total))
