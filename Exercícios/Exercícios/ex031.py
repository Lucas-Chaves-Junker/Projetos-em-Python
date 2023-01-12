distancia = float(input('Qual a distância da sua viagem? '))
if distancia <= 200:
    custo = distancia * 0.50
    print('O preço da sua passagem é R${:.2f} '.format(custo))
else:
    custo1 = km_viagem * 0.45
    print('O preço da sua passagem é R${:.2f}' .format(custo1))