jogador = {}
partida = []

jogador['Nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))

print('-=-' * 13)
for c in range(0, tot):
    partida.append(int(input(f'   Quantos gols na partida {c}? ')))
jogador['Gols'] = partida[:]
jogador['Total'] = sum(partida)
print('-=-' * 13)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')

print('-=-' * 13)
print(f'O jogador {jogador["Nome"]} jogou {len(jogador["Gols"])} partidas.')

for k, v in enumerate(jogador['Gols']):
    print(f'   => Na partida {k}, fez {v} gols.')
print(f'Foi um total de {sum(partida)} gols')
