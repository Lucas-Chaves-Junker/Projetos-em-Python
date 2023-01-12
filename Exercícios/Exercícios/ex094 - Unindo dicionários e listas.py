cadastro = []
pessoa = {}
soma = media = 0
while True:
    pessoa['Nome'] = str(input('Nome: '))
    pessoa['Idade'] = int(input('Idade: '))
    soma += pessoa['Idade']
    while True:
        pessoa['Sexo'] = str(input('Sexo : ')).upper()
        if pessoa['Sexo'] in 'MF':
            break
        print('ERRO! Por favor digite apenas M ou F.')
    cadastro.append(pessoa.copy())

    while True:
        resp = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
        if resp in 'SN':
            break
        print('ERRO! Por favor digite apenas S ou N.')
    if resp == 'N':
        break

    pessoa.clear()
media = soma / len(cadastro)
print(f'Todos {cadastro}')
print(f' - O grupo tem {len(cadastro)} pessoas')
print(f' - A média de idade é de {media:.2f} anos')
print(f' - As mulheres cadastradas foram: ', end=' ')

for f in cadastro:
    if f['Sexo'] in 'F':
        print(f['Nome'], end=' ')
print('  \n - Lista das pessoas que estão acima da média:')

for p in cadastro:
    if p['Idade'] >= media:
        print('    ')
        for c, f in p.items():
            print(f'{c} = {f}', end=' ')
        print()
print('<< ENCERRADO >>')
