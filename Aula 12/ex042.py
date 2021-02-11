print('Informe os comprimeto de três retas e veja se é possível formar um triângulo e qual o tipo de triângulo!')

colors = {
    'limpo': '\033[m',
    'verd': '\033[1;32m',
    'azul': '\033[1;34m',
    'amar': '\033[1;33m',
    'verm': '\033[1;31m'
}

retas = [float(input('Digite (em cm) o comprimento da {}primeira reta{}: '.format(colors['verm'], colors['limpo']))),
         float(input('Digite (em cm) o comprimento da {}segunda reta{}: '.format(colors['azul'], colors['limpo']))),
         float(input('Digite (em cm) o comprimento da {}terceira reta{}: '.format(colors['verd'], colors['limpo'])))]

if retas[0] <= retas[1] + retas[2] and retas[1] <= retas[0] + retas[2] and retas[2] <= retas[0] + retas[1]:
    print('\nÉ possível formar um triangulo com as retas de {1}{4:.2f}cm{0}, {2}{5:.2f}cm{0} e {3}{6:.2f}cm{0}.'
          .format(colors['limpo'], colors['verm'], colors['azul'], colors['verd'], retas[0], retas[1], retas[2]))

    if retas[0] == retas[1] == retas[2]:
        print('E pelo fato de todas as retas terem o mesmo comprimento,\n'
              'o triangulo é do tipo {}EQUILÁTERO{}!'.format(colors['amar'], colors['limpo']))

    elif retas[0] != retas[1] != retas[2] != retas[0]:
        print('E pelo fato de todas as retas terem diferentes comprimentos,'
              '\no triangulo é do tipo {}ESCALENO{}!'.format(colors['amar'], colors['limpo']))

    else:
        print('E pelo fato de duas retas serem iguais e uma diferente,\n'
              'o triangulo é do tipo {}ISÓSCELES{}!'.format(colors['amar'], colors['limpo']))

else:
    print('Não é possível formar um triangulo!')
