import random
aluno1=input('Primeiro aluno:')
aluno2 = input('Segundo aluno: ')
alno3 = input('Terceiro aluno: ')
aluno4 = input('Quarto aluno: ')
lista = [aluno1,aluno2,alno3,aluno4]
random.shuffle(lista)

print('A prdem de apresentação sera')
print(lista)