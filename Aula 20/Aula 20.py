# Exemplo 1
print('\033[1;31mExemplo 1\033[0m\n')


def linha():
    print('-' * 80)


def mostraNome(nome):
    print(f'Olá {nome}, tenha um bom dia.')


# Main
mostraNome('Lucas')


# Exemplo 2
linha()
print('\n\033[1;31mExemplo 2\033[0m\n')


def multi(a, b):
    m = a*b
    print(f'{a} * {b} = {m}')


# Main
multi(2, 5)
multi(3, 7)
multi(9, 9)

# Exemplo 3
linha()
print('\n\033[1;31mExemplo 3\033[0m\n')


def contador(* n):
    # Ao definir a função com o * antes do parametro, podemos colocar N valores. Chamamos isso de desempacotamento.
    print(f'Foram recebidos os números {str(n).replace("(", "").replace(")", "")}. Total de {len(n)} números.')


#Main
contador(6, 2, 8, 7, 7)

# Exemplo 4
linha()
print('\n\033[1;31mExemplo 4\033[0m\n')


def somaN(* n):
    s = sum(n)
    print(f'A soma dos valores {n} é igual a {s}')


# Main
somaN(1, 2, 3, 4, 5)

# Exemplo 5
linha()
print('\n\033[1;31mExemplo 5\033[0m\n')


# É possivel passar uma lista como parametro
def dobro(lst):
    # Estou utilizando while, pois não funcionou com for
    i = 0
    while i < len(lst):
        lst[i] *= 2
        i += 1


# Main
nums = [1, 2, 3, 4, 5]
print(nums)
dobro(nums)
print(nums)





















