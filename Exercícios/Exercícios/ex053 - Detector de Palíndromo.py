frase = str(input('Escreva uma frase. ')).upper().strip()
junto = frase.replace(' ', '')
inverter = ''

for letra in range(len(junto) - 1, -1, -1):
    inverter += junto[letra]
if inverter == junto:
    print('\nÉ um palíndromo')
else:
    print('\nNão é um palíndromo')
