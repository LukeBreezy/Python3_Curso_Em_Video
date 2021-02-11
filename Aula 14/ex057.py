sexo = ''

while 'M' != sexo != 'F':   # Enquanto a pessoa não digitar uma opção válida, o laço não para
    if sexo != '':
        print('{} não é uma opção válida, digite M para masculino ou F para feminino.\n'.format(sexo))
    sexo = input('Qual é o seu sexo? [M/F]: ').upper()

if sexo == 'M':
    print('Você é um homem.')
else:
    print('Você é uma mulher.')
