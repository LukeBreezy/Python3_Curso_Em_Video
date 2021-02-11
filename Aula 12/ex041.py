from datetime import date

colors = {
    'limpo': '\033[m',
    'roxo': '\033[1;35m',
    'verd': '\033[1;32m',
    'azul': '\033[1;34m',
    'amar': '\033[1;33m',
    'verm': '\033[1;31m',
    'cinz': '\033[1;37m'
}

print('Informe o ano de nascimento para verificar qual é a sua categoria, segundo a Confederação Nacional de Natação!')

idade = date.today().year - int(input('Digite o ano de nascimento: '))

if 0 < idade <= 9:
    print('Idade: {}\nCategoria: {}MIRIM{}'.format(idade, colors['roxo'], colors['limpo']))
elif 9 < idade <= 14:
    print('Idade: {}\nCategoria: {}INFANTIL{}'.format(idade, colors['azul'], colors['limpo']))
elif 14 < idade <= 19:
    print('Idade: {}\nCategoria: {}JUNIOR{}'.format(idade, colors['verd'], colors['limpo']))
elif 19 < idade <= 20:
    print('Idade: {}\nCategoria: {}SENIOR{}'.format(idade, colors['amar'], colors['limpo']))
elif idade > 20:
    print('Idade: {}\nCategoria: {}MASTER{}'.format(idade, colors['cinz'], colors['limpo']))
else:
    print('{}Ano de nascimento não pode ser maior que o ano atual!'.format(colors['verm']))
