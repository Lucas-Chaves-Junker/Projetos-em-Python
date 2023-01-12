print('{:=^40}'.format(' \033[0;31mLOJAS INDIANAS \033[m'))

produto = float(input('Preço das compras: R$'))
print('''\nFORMAS DE PAGAMENTO 
1-À vista dinheiro ou PIX.
2-À vista no cartão.
3-Em ate 2x no cartao:
4-Em 3x ou mais no cartão''')
opcao = int(input('\nqual a forma de pagamento? '))
parcelas = int(input('Quantas parcelas? '))

if opcao == 1:
    avista = produto - (produto * 0.1)
    print('O Produto á vista custa R${:.2f}'.format(avista))
elif opcao == 2:
    cartao = produto - (produto * 0.05)
    print('O Produto á vista no cartão custa R${:.2f}'.format(cartao))
elif opcao == 3:
    print('O Produto 2x no cartão custa R${:.2f}'.format(produto))
elif opcao == 4:
    cartao = produto + (produto * (0.20 * parcelas))
    print('O Produto 3x no cartão custa R${:.2f}'.format(cartao))
else:
    print('OPÇÃO INVALIDA de pagamento tente novamente')
