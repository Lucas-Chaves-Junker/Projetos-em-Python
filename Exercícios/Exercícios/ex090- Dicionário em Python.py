alunos = {}

alunos['Nome'] = str(input('Digite o nome do aluno: '))
alunos['Média'] = float(input(f'Digite a média do aluno: {alunos["Nome"]} '))

if alunos['Média'] >=7 :
    alunos['situação'] = 'Aprovado'
elif alunos['Média'] <7 :
    alunos['situação'] = 'Recuperação'
else:
    alunos['situação'] = 'Reprovado'

for c, k in alunos.items():
    print(f'{c} é igual a {k}')
