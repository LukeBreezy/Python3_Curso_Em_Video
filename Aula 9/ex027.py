nome = input('Digite o seu nome completo: ').title()

print('''
Primeiro nome: {}
Ultimo nome: {}
'''.format(nome.split()[0], nome.split()[len(nome.split()) - 1]))
