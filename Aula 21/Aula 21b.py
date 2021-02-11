def linha():
    print('\033[1;33m=-' * 50, '\033[0m')


# =-=-=-=  RETORNANDO VALORES (return)  =-=-=-=

# Ao usar um return em uma função, podemos utilizar no escopo global, o valor gerado por ela
def soma(a=0, b=0, c=0):
    s = a + b + c
    return s


res = soma(10, 5, 2)
print(res)
linha()
print(f'Foram realizadas 3 somas e os resultados são: {soma(10, 5, 2)}, {soma(20, 9, 3)} e {soma(17, 3, 5)}')
linha()

# Outro exemplo


def par(n=0):
    """
    Diz se o número é par ou ímpar.
    :param n: Valor passado pelo usuário, e é 0 por padrão.
    :return: bool
    """
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print(f'{num} é par.')
else:
    print(f'{num} não é par.')
