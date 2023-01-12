salario = float(input('Qual é o salário do funcionário? R$'))
aumento_salario = salario + (salario * 0.15)

print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a ganhar R${:.2f}'.format(salario,aumento_salario))