somaidade = 0
mediaidade = 0
idade2 = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 =0


for p in range(1, 5):
    print('------ {}º PESSOA ------'.format(p))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M | F]:')).upper().strip()

    somaidade += idade

    if p == 1 and sexo == 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'M'and maioridadehomem< idade:
        maioridadehomem = idade
        nomevelho = nome


    if idade < 20 and sexo == 'F':
        totmulher20 = +1

mediaidade = somaidade / 4
print('A média das idades é {} anos'.format(mediaidade))
print('O homem mais velho tem {} de idade e se chama {} '.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))
