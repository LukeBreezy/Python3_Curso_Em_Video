lanche = ['Hamburguer', 'Suco', 'Pizza', 'Sorvete']
print('\033[1;33mlanche \033[0m=', lanche)

# INSERINDO CONTEUDO EM UMA LISTA

# append() -> insere o valor no final da lista
lanche.append('Biscoito')
print("\033[1;33mlanche.append('Biscoito') \033[0m=", lanche)

lanche.append('Torta')
print("\033[1;33mlanche.append('Torta') \033[0m=", lanche)

# insert() -> insere o valor na posição indicada
lanche.insert(0, 'Hot-Dog')
print("\033[1;33mlanche.insert(0, 'Hot-Dog') \033[0m=", lanche)

lanche.insert(3, 'Batata Frita')
print("\033[1;33mlanche.insert(3, 'Batata Frita') \033[0m=", lanche)

lanche.insert(5, 'Esfiha')
print("\033[1;33mlanche.insert(5, 'Esfiha') \033[0m=", lanche)

lanche.insert(7, 'Bolo')
print("\033[1;33mlanche.insert(7, 'Bolo') \033[0m=", lanche)

# REMOVENDO CONTEUDO DE UMA LISTA

# del -> apaga valores armazenados, em listas usa o indice como referencia
del lanche[4]
print("\033[1;33mdel lanche[4] \033[0m=", lanche)

del lanche[lanche.index('Hamburguer')]
print("\033[1;33mdel lanche[lanche.index('Hamburguer')] \033[m=", lanche)

# pop() -> apaga o ultimo valor armazenado na lista ou o valor no indice indicado
lanche.pop(0)
print("\033[1;33mlanche.pop(0) \033[0m=", lanche)

lanche.pop()
print("\033[1;33mlanche.pop() \033[0m=", lanche)

# remove() -> apaga o valor da lista, usando o conteudo como referencia
lanche.remove('Sorvete')
print("\033[1;33mlanche.remove('Sorvete') \033[0m=", lanche)

lanche.remove('Batata Frita')
print("\033[1;33mlanche.remove('Batata Frita') \033[0m=", lanche)

if 'Bolo' in lanche:
    lanche.remove('Bolo')
    print("""\033[1;33mif 'Pizza' in lanche:
    lanche.remove('Pizza') \033[0m=""", lanche)

# CRIANDO UMA LISTA DE NÚMEROS RAPIDAMENTE

# list(range()) -> cria uma lista de números em ordem crescente dentro de um intervalo, e pode determinar a progressão
n1 = list(range(0, 11))
print("\033[1;33mn1 = list(range(0, 11)) = \033[0m", n1)

n2 = list(range(0, 11, 2))
print("\033[1;33mn2 = list(range(0, 11, 2)) \033[0m=", n2)

# sort() -> organiza uma lista em ordem crescente ou decrescente e salva ela em ordem
n3 = [2, 8, 3, 7, 9, 1, 6]
print("\033[1;33mn3 \033[0m=", n3)

n3.sort()
print("\033[1;33mn3.sort() \033[0m=", n3)

n3.sort(reverse=True)
print("\033[1;33mn3.sort(reverse=True) \033[0m=", n3)

# sorted() -> organiza uma lista em ordem crescente ou decrescente mas não salva ela em ordem
n4 = [6, 8, 4, 9, 1, 3, 1]
print("\033[1;33mn4 \033[0m=", n4)

print("\033[1;33mprint(sorted(n4)) \033[0m=", sorted(n4))
print("\033[1;33mprint(sorted(n4, reverse=True)) \033[0m=", sorted(n4, reverse=True))

# len -> retorna o tamanho da lista
print("\033[1;33mlen(n3) \033[0m=", len(n3))

# enumerate() -> faz uma iteração e representa as posições de uma lista e a propria lista
for i, n in enumerate(n4):
    print("")


