print('--==--' * 12)
print('ANALISADOR DE TRIÂNGULOS')
print('--==--' * 12)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento:'))
r3 = float(input('Terceiro segmento: '))

if (r1 < r2 + r3) and (r2 < r3 + r1) and (r3 < r2 + r1):
    print('Os segmentos acima podem formar trinângulo.')
else:
    print('Os segmentos acima NÂO PODEM FORMAR triângulo.')
