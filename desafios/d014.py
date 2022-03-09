from math import radians, sin, cos, tan
an = float(input('Digite o ângulo: '))
seno = sin(radians(an))
print('O ângulo de {} tem seno de {:.2f}'.format(an, seno))
cos = cos(radians(an))
print('O âmgulo de {} tem cosseno de {:.2f}'.format(an, cos))
ta = tan(radians(an))
print('O Ângulo de {} tem tangente de {:.2f}'.format(an, ta))
