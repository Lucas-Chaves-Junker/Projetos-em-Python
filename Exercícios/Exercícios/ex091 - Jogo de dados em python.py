from random import randint
from time import sleep
from operator import itemgetter

ranking = []

cont = 1
print('Valores sorteados: ')
dado = {}
for c in range(1, 5):
    dado[f'jogador{c}'] = randint(1, 6)

for d, k in dado.items():
    print(f'     O {d} tirou {k} ')
    sleep(1)
print('Ranking dos jogadores: ')
# ordenando o dicionário
for i in sorted(dado, key=dado.get, reverse=True):
    sleep(1)
print(f'     {cont}° lugar {i} com {dado[i]}')
cont += 1
# outra forma de organizar
'''ranking = sorted(dado.items(),key=itemgetter(1), reverse=True)
for k,v in enumerate(ranking):
    print(f'     {k+1}° lugar {v[0]} com {v[1]}')'''
