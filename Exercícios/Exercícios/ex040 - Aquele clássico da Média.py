nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print('A média das notas {} e {} é {}'.format(nota1,nota2,media))

if media < 5:
    print('\033[31m=== REPROVADO ===\033[31m')
elif media >= 5 and media <= 5.9:
    print('\033[31m=== RECUPERAÇÃO ===\033[31m')
elif media >= 7 and media <= 10:
    print('\033[31m=== APROVADO ===\033[31m')
