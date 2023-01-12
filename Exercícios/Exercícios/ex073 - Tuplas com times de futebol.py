times = ('Flamengo', 'Palmeiras', 'Atlético Mineiro', 'Grêmio', 'Athletico Paranaense', 'Santos',
         'São Paulo', 'Internacional', 'Fluminense', 'Corinthians', 'Fortaleza', 'Bahia', 'Ceará',
         'Cruzeiro', 'América Mineiro', 'Atlético Goianiense', 'Chapecoense', 'Botafogo', 'Vasco da Gama',
         'Red Bull Bragantino')
print('-=-'*13)
print('Lista de tímes do Brasileirão')
print('-=-'*13)

print(f'Os cinco primeiros colocados são : {times[0:5]}')
print(f'Os ultimos quatro colocados são : {times[-4:]}')
print(f'Os times em ordem alfabetica : {sorted(times)}')
print('O Bahia está na posição : {}'.format(times.index('Bahia')+1))
