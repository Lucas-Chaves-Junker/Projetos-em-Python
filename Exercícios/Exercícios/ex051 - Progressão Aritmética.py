print('==' * 10)
print('10 TERMOS DE UMA PA')
print('==' * 10)

primeiro_termo = int(input('PRIMEIRO TERMO: '))
razao = int(input('RAZÃO: '))
termo = 0

for cont in range(1, 11, 1):
    termo = primeiro_termo + ((cont - 1) * razao)
    print('{} ->'.format(termo), end=' ')
print('ACABOU!')
