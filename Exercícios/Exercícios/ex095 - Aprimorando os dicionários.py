jogador = {}
partida = []
time = []
while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    partida.clear()

    print('---' * 13)
    for c in range(0, tot):
        partida.append(int(input(f'   Quantos gols na partida {c + 1}? ')))
    jogador['Gols'] = partida[:]
    jogador['Total'] = sum(partida)
    time.append(jogador.copy())
    print('---' * 13)

    while True:
        resp = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
        if resp in 'SN':
            break
        print('ERRO! Por favor digite apenas S ou N.')
    if resp == 'N':
        break
print('---' * 13)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('---' * 13)

for k, v in enumerate(time):
    print(f'{k:<4}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()

while True:
    print('---' * 13)
    busca = int(input('Mostre os dados de qual jogador? (999 para parar) '))

    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não exite jogador com codigo {busca}! ')
    else:
        print(f'---- LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}')
        for l, g in enumerate(time[busca]["Gols"]):
            print(f'    No jogo {l + 1} fez {g} Gols')
