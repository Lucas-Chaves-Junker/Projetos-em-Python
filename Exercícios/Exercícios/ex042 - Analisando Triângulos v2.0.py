print('-=-' * 12)
print('\033[0;31mANALISADOR DE TRIÂNGULOS\033[m')
print('-=-' * 12)
m1 = float(input('Primeiro segmento: '))
m2 = float(input('Segundo segmento: '))
m3 = float(input('Terceiro segmento: '))

if (m1 < m2 + m3) and (m2 < m1 + m3) and (m3 < m1 + m2):
    print('Os segmentos acima podem formar um trinângulo.', end=' ' )

    if (m1 == m2) and (m2 == m3):
        print('EQUILÁTERO ')

    elif (m1 == m2 != m3) or (m1 == m3 != m2) or (m2 == m3 != m1):
        print('ISÓSCELES ')

    else:
        print('ESCALENO ')

else:
    print('Os segmentos acima NÂO PODEM FORMAR triângulo.')
