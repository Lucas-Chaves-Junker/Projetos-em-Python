altura = float(input('Qual é a altura da parede? '))
largura = float(input('Qual é a largura da parede? '))

area = altura * largura
quant_tinta = area / 2

print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²\n'
      'e para pintar essa parede são necessarios {:.2f}L de tinta'.format(altura, largura,area,quant_tinta))
