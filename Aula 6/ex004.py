x = input('Digite algo: ')
print(type(x))
print('{} é numérico'.format(x) if x.isnumeric() is True else '{} não é numérico'.format(x))
print('{} é um número decimal'.format(x) if x.isdecimal() is True else '{} não é número decimal'.format(x))
print('{} é uma letra'.format(x) if x.isalpha() is True else '{} não é uma letra'.format(x))
print('{} é alfanumérico'.format(x) if x.isalnum() is True else '{} não é alfanumérico'.format(x))
print('{} faz parte da tabela ASCII'.format(x) if x.isascii() is True else '{} não faz parte da tabela ASCII'.format(x))
print('{} está em maiúsculas'.format(x) if x.isupper() is True else '{} não está em maiúsculas'.format(x))
print('{} está em minusculas'.format(x) if x.islower() is True else '{} não está minusculas'.format(x))
print('{} está capitalizado'.format(x) if x.istitle() is True else '{} não está capitalizado'.format(x))