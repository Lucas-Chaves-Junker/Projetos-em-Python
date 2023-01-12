def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno {largura} X {comprimento} é de {a}m².')


# Programa principal
print(' Controle de Terrenos')
print('---' * 7)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
