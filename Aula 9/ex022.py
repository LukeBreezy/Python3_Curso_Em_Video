nome = input('Digite seu nome completo: ')

print('Nome em maiúsculas: {}'.format(nome.upper()))
print('Nome em minúsculas: {}'.format(nome.lower()))
print('Tamanho do nome sem espaços: {}'.format(len(nome.replace(' ', ''))))
print('Tamanho do primeiro nome: {}'.format(len(nome.split()[0])))
