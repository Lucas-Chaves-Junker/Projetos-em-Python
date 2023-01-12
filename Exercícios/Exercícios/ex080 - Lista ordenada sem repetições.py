lista = []

for c in range(1, 6):
    n = int(input(f'Digite o {c} número:'))

    if c == 1 or n > lista[len(lista) - 1]:
        lista.append(n)
        print('Foi adicíonado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos}° da lista')
                break
            pos += 1
print(f'Os valores digitados em ordem foram: {lista}')
