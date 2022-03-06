n = int(input('Digite um número para criar uma tabuada: '))
c = 0
print('{:=^20}'.format('Tabuada'))
while (c < 10):
    c += 1
    print('{} * {} = {}'.format(n, c, n * c))
