ficha = []
n1 = n2 = 0
while True:
    # ENTRADA DE DADOS
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2:'))
    media = (n1 + n2) / 2
    ficha.append([nome, [n1, n2], media])
    # verificação
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == "N":
        break

# BOLETIM FORMATADO
print('-=' * 15)
print(f'{"n°.":<4}{"NOME":<10}{"MEDIA":>8}')
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

# VERIFICAR NOTA DE ALUNO
while True:
    print('-=' * 15)
    opc = int(input('Mostrar nota de qual aluno? (999 interrompe): '))
    if opc == 999:
        break
    if opc <= len(ficha):
        print(f'notas de {ficha[opc][0]} sao: {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')
