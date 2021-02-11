n = input('Digite algo: ')
print(n)
if n.isnumeric():
    print('{} é numerico'.format(n))
elif n.isalpha():
    print('{} é letra'.format(n))
elif n.isalnum():
    print('{} é alfanumerico'.format(n))
elif n.isascii():
    print('{} é um caractere da tabela ASCII'.format(n))

