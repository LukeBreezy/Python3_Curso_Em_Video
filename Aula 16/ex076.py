prod = ('PlayStation 5', 4699, 'God Of War', 250, 'Caderno', 25, 'Lapis', 1.5, 'Pizza', 27.5, 'Refrigerante', 5)

print(f"""{'':-^37}
{'PRODUTOS':^37}
{'':-^37}""")

for i in range(0, len(prod), 2):
    print(f'{prod[i]:.<25} R$ {f"{prod[i+1]:8.2f}".replace(".", ",")}')

print(f'{"":-^37}')
