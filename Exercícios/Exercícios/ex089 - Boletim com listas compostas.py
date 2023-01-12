alunos = []
nomes = []
notas = []
a = ' '
n1 = n2 = soma = media = 0
while True:
    nomes.append(str(input('Digite seu nome: ')))
    notas.append(float(input('Digite a primeira nota: ')))
    notas.append(float(input('Digite a segunda nota: ')))
    nomes.append(notas[:])
    alunos.append(nomes[:])
    nomes.clear()
    notas.clear()

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
# mostra a nota nos
for c, f in enumerate(alunos):
    for i in range (1,2):
        print(alunos[c][i])

'''print(alunos)
print(alunos[0][1][0])
print(alunos[0][1][1])'''
