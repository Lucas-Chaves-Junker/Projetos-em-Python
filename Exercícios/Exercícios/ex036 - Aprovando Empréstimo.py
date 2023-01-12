val_casa = float(input('Qual o valor do imóvel? '))
salario = float(input('Sálario do comprador: R$'))
anos = int(input('Quantos anos de financiamento?: '))
prestacao = val_casa / (anos * 12)
porcnt_salario = salario * 0.30

print('Para pagar uma casa de R$ {:.2f} em {} anos'.format(val_casa,anos), end =' ')
print('a prestação sera de R${:.2f}'.format(prestacao))
if prestacao <= porcnt_salario:
    print('Emprestimo aprovado!')
else:
    print('Infelizmente o emprestimo foi negado!')
