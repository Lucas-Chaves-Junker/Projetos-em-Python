palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO',
            'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

for p in palavras:
    print(f'\nna palavra {p} temos ', end=' ')
    for letra in p:
        if letra in 'AEIOU':
            print(letra, end=' ')
