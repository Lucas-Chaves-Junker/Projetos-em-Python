velocidade = int(input('Qual a velocidade atual do carro? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('MULTADO! Você excedeu o limite de velocidade permitido que é de 80km/h\n'
          'Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um Bom Dia! Dirija com segurança!')

