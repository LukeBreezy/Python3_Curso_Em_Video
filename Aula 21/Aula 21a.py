def linha():
    print('\033[1;33m=-' * 50, '\033[0m')


# =-=-=-=  INTERACTIVE HELP  =-=-=-=
print('=-=-=-=  INTERACTIVE HELP  =-=-=-=')
# O help() nos descreve como funcionam os comandos Python, como os exemplos abaixo
help(print())
linha()
print(input.__doc__)
linha()
help(input)
linha()
# Basicamente, o help nos mostrara o DOCSTRING(documentação) das funções internas

# =-=-=-=  DOCSTRINGS  =-=-=-=
print('=-=-=-=  DOCSTRINGS  =-=-=-=')
# Esta é uma função que eu criei
def contador(inicio, fim, passo=0):
    # Abaixo esta uma descrição de como a função funciona, sendo assim, será meu DOCSTRING
    """
    Faz uma contagem de inicio até fim, pulando de passo em passo.
    :param inicio: Número de onde a contagem parte;
    :param fim: Número onde a contagem deve parar;
    :param passo: Determina a progressão da contagem, e caso não receba nada, será 0 por padrão;
    :return: Sem retorno.
    """
    if (inicio > fim and passo > 0) or (inicio < fim and passo < 0):
        passo *= -1
    elif passo == 0:
        passo = 1

    print('\033[0m=' * 50, '\033[0m')
    print(f'Contagem de {inicio} até {fim} de {abs(passo)} em {abs(passo)}.')
    for i in range(inicio, (fim+1 if fim > inicio else fim-1), passo):
        print(i, end=' ', flush=True)
    print('FIM.')

help(contador)
linha()

# =-=-=-=  ESCOPO DE VARIÁVEIS  =-=-=-=

# Local onde a variável vai existir e onde não vai existir
def multi():
    # A variável m, abaixo, é uma variável local. Portanto só pode ser acessada dentro da função, mas não fora dela.
    # Ou seja, tem um escopo local
    m = A * B
    print(f'{A} * {B} = {m}')

# As variáveis A e B, abaixo, são variáveis globais. Portanto pode ser acessada em qualquer parte do programa.
# Ou seja, tem um escopo global
A, B = 10, 20
multi()
linha()

def teste(b):
    a = 8       # Existe essa mesma variavel do lado de fora da função, mas o Python vai priorizar a local.
    b += 5      # Esta variavel é passada no parametro, que no caso será o A global, portanto o local não vai interfeir.
    c = 3       # Esta variável é local, e neste exemplo não teve nenhuma interação vinda de fora da função.
    print(f'A dentro da função vale {a}')
    print(f'B dentro da função vale {b}')
    print(f'C dentro da função vale {c}')


a = 5
teste(a)
print(f'A fora vale {a}')
linha()

# Ainda usando o exemplo acima, porém com algumas alterações
def teste(b):
    global a    # Ao usar o global, o Python entende que não queremos criar a variável A local, mas sim usar a A global;
    a = 8       # Portanto, esta variável, será diretamente afetada no escopo global.
    b += 5      # Esta variavel recebe o valor passado no parametro;
                # sendo assim, o valor de A passado depois do parametro, não vai alterar B.
    c = 3       # Esta variável é local, e neste exemplo não teve nenhuma interação vinda de fora da função.
    print(f'A dentro da função vale {a}')
    print(f'B dentro da função vale {b}')
    print(f'C dentro da função vale {c}')


a = 5
teste(a)
print(f'A fora vale {a}')
linha()
