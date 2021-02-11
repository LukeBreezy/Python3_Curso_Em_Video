frase = input('Digite uma frase qualquer: \n').upper().strip()

print('A letra "A" aparece {} vezes na sua frase'.format(frase.count('A')))
print('Ela aparece pela primeira vez na posição {}'.format(frase.find('A') + 1))
print('E aparece pela ultima vez na posição {}'.format(frase.rfind('A') + 1))
