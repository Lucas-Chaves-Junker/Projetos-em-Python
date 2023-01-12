from random import choice
nome = input('Primeiro nome: ')
nome1 = input('segundo nome: ')
nome2 = input('terceiro nome: ')
nome3 = input('quarto nome: ')
lista =[nome,nome1,nome2,nome3]
escolhido = choice(lista)

print('O escolhido foi {}'.format(escolhido))