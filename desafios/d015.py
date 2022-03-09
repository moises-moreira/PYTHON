from random import choice
n1 = str(input('primeira pessoa: '))
n2 = str(input('segunda pessoa: '))
n3 = str(input('terceira pessoa: '))
n4 = str(input('quarta pessoa: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)

print('O aluno escolhido foi {}'.format(escolhido))
