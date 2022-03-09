from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adijacente: '))
hi = hypot(co, ca)
print('hipotenusa {:.2f}'.format(hi))
