def ficha(n='<Desconhecido>', g=0):
    print(f'O jogador {n} fez {g} no campeonato.')


nome = str(input('Nomedo jogador: '))
gols = str(input('Quantidade de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(g=gols)
else:
    ficha(nome, gols)
