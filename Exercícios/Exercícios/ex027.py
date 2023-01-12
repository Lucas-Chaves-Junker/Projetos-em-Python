nomecplt: str = str(input('Digite seu nome completo: ')).strip()
nome = nomecplt.split()
print('\nMuito prazer em te conhecer!')
print('Seu primeiro nome é {}\nSeu último nome é {}'.format(nome[0], nome[len(nome) - 1]))


