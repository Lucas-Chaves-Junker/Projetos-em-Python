import datetime

atual = datetime.date.today().year
totmaior = 0
totmenor = 0

for c in range(1, 8):
    nasc = int(input('Em que anos a {}º pessoa nasceu? '.format(c)))
    idade = atual - nasc
    if idade <= 20:
        totmenor += 1
    else:
        totmaior += 1

print('''Ao todo tivemos {} pesoas maiores de idade.
E também tivemos {} pessoas menores de idade.'''.format(totmaior, totmenor))
