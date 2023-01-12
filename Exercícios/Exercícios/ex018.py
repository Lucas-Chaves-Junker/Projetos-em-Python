import math
angulo = float(input("Diginte o angulo desejado: "))
math.radians(angulo)
seno = math.sin(math.radians(angulo))
coss  = math.cos(math.radians(angulo))
tang =  math.tan(math.radians(angulo))

print('O seno, cosseno e tangente de {}º são:\nSeno: {:.2f} \nCosseno: {:.2f} \nTangente: {:.2f}'.format(angulo,seno,coss,tang))