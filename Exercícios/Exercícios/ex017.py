import math

cat_adj = float(input('Comprimento do cateto adjacente: '))
cat_opos = float(input('Comprimento do cateto aposto: '))
hipotenusa = math.hypot(cat_opos, cat_adj)

print('A hipotenusa vale: {:.2f} '.format(hipotenusa))
