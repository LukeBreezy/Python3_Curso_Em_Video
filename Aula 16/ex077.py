palavras = ('Garrafa', 'Celular', 'Mouse', 'Mesa', 'Computador', 'Tela', 'Python', 'Programar')

for i in palavras:
    print(f'\nA palavra \033[1;32m{i.upper()}\033[0m tem as vogais: ', end='')
    for j in i.upper():
        if j in 'AEIOU':
            print(f'\033[1;33m{j.upper()}\033[0m', end=' ')
