frase = str(input('Digite uma frase: ')).lower()
print('A letra [a] aparece {} vezez na fase {}'.format(frase.count('a'), frase))
print('A primeira letra [a] apareceu na posição {}'.format(frase.find('a')+1))
print('A última letra [a] apareceu na posição {}'.format(frase.rfind('a')+1))