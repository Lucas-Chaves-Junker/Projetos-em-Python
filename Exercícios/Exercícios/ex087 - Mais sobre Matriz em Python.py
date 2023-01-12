matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = scol = 0
maior = 0
# lendo os valores da matriz
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

        # somando os números pares da matriz
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]

        # soma dos valores da terceira coluna
        if c == 2:
            scol += matriz[l][c]

        # verificândo o maior numero na segunda linha
        if l == 1 and c == 0:
            maior = matriz[l][c]
        else:
            if matriz[l][c] > maior and l == 1:
                maior = matriz[l][c]

# Imprimindo a matriz na tela
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()
print('-=-' * 14)
print(f'A soma dos valores pares é {spar}')
print(f'A soma dos valores terceira coluna  é {scol}')
print(f'O maior valor da segunda linha é  {maior}')
