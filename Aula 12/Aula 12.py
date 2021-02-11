nome = input('Digite seu nome: ').capitalize()
if nome == 'Ingrid':
    print('Seu nome é muito bonito!')
elif nome in 'Lucas Luke Breezy':
    print('Tu é muito foda!!!')
else:
    print('Seu nome é bem normal')

print('Tenha um bom dia {}{}{}!!!'.format('\033[1;5;34m', nome, '\033[m'))
