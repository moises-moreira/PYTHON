from posixpath import split


num = str(input('Digite um número de 0 a 9999: ')).strip()
print('Unidade: {}'.format(num[3]))
print('Dezena: {}'.format(num[2]))
print('Centena: {}'.format(num[1]))
print('Milhar: {}'.format(num[0]))
