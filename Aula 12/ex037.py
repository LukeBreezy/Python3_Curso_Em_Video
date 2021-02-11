num = int(input('Digite um número inteiro, e veja a conversão para a base numerica desejada: '))
aux = num
colors = {
    'limpo': '\033[m',
    'roxo': '\033[1;35m',
    'bran': '\033[1;30m',
    'azul': '\033[1;34m',
    'amar': '\033[1;33m',
    'verm': '\033[1;31m'
}

base_num = int(input('''
Converter para:
1 - Binário
2 - Octal
3 - Hexadecimal
'''))

if base_num == 1:    # Decimal para Binário
    print('''Explicacao...
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                     ___ 25 % 2 == {3}1{0}
                 ___|______ 12 % 2 == {2}0{0}
             ___|___|_________ 6 % 2 == {1}0{0}
         ___|___|___|____________ 3 % 2 == {5}1{0}
     ___|___|___|___|_______________ 1 % 2 == {4}1{0}
    |   |   |   |   |
    {4}1   {5}1   {1}0   {2}0   {3}1{0}
    
    25 == 11001
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''.format(colors['limpo'], colors['verm'], colors['azul'], colors['bran'], colors['amar'], colors['roxo']))

    bin_logica = []
    bin_metodo = bin(aux)

    while aux >= 1:
        bin_logica.insert(0, aux % 2)
        aux = aux // 2

    bin_logica = str(bin_logica).replace(', ', '').replace(']', '').replace('[', '')

    print('''Seguindo a linha de raciocínio acima, conclui-se que a conversão de {1}{2}{0}
    da base decimal para a base bínaria é igual à {1}{3}{0}'''.format(colors['limpo'], '\033[1;4;37m', num, bin_logica))

    print('Conversão lógica:', bin_logica)
    print('Conversão método:', bin_metodo[2:])
    
elif base_num == 2:    # Decimal para Octal
    print('''Explicacao...
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                 ___ 687 % 8 == {2}7{0}
             ___|______ 85 % 8 == {1}5{0}
         ___|___|_________ 10 % 8 == {4}2{0}
     ___|___|___|____________ 1 % 8 == {3}1{0}
    |   |   |   |
    {3}1   {4}2   {1}5   {2}7{0}
    
    687 == 1257
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''.format(colors['limpo'], colors['verm'], colors['azul'], colors['amar'], colors['roxo']))

    oct_logica = []
    oct_metodo = oct(aux)

    while aux >= 1:
        oct_logica.insert(0, aux % 8)
        aux = aux // 8

    oct_logica = str(oct_logica) \
        .replace('[', '').replace(']', '') \
        .replace(', ', '')

    print('''Seguindo a linha de raciocínio acima, conclui-se que a conversão de {1}{2}{0}
    da base decimal para a base octal é igual à {1}{3}{0}'''.format(colors['limpo'], '\033[1;4;37m',num, oct_logica))

    print('Conversão lógica:', oct_logica)
    print('Conversão método:', oct_metodo[2:])

elif base_num == 3:    # Decimal para Hexadecimal
    print('''Explicacao...
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                 ___ 55327 % 16 == {2}15{0} -> {2}F{0}
             ___|______ 3457 % 16 == {1}1{0}
         ___|___|_________ 216 % 16 == {4}8{0}
     ___|___|___|____________ 13 % 16 == {3}13{0} -> {3}D{0}
    |   |   |   |
    {3}D   {4}8   {1}1   {2}F{0}
    
    55327 == D81F
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''.format(colors['limpo'], colors['verm'], colors['azul'], colors['amar'], colors['roxo']))

    hex_logica = []
    hex_metodo = hex(aux).upper()

    while aux >= 1:
        hex_logica.insert(0, aux % 16)
        aux = aux // 16

    hex_logica = str(hex_logica) \
        .replace(']', '').replace('[', '') \
        .replace('10', 'A').replace('11', 'B') \
        .replace('12', 'C').replace('13', 'D') \
        .replace('14', 'E').replace('15', 'F') \
        .replace(', ', '')

    print('''Seguindo a linha de raciocínio acima, conclui-se que a conversão de {1}{2}{0}
da base decimal para a base hexadecimal é igual à {1}{3}{0}'''.format(colors['limpo'], '\033[1;4;37m',num, hex_logica))

    print('Conversão lógica:', hex_logica)
    print('Conversão método:', hex_metodo[2:])
