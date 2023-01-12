salario = float(input('Qual é o salário do funcionário? R$'))

if salario > 1250:
    aumento = (salario * 0.10) + salario
    print('O salario R${} teve um aumento de 10% e agora é R${}'.format(salario, aumento))
else:
    aumento = (salario *0.15) + salario
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(salario,aumento))