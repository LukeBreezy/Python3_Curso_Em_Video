print('{:=^30}'.format('Palindromo'))

colors = {
    'limpo': '\033[0m',
    'amar': '\033[1;33m',
    'azul': '\033[1;34m'
}

txt = input('Digite uma palavra ou frase, e veja se é um palindromo: ')
txt = ''.join(txt.upper().split())
rever = txt[::-1]

# OU
# for i in range(len(txt)-1, -1, -1):
#    rever += txt[i]

if txt == rever:
    print('{3}{0}{2} lido de trás para frente é {4}{1}{2}, portanto é um palindromo!'
          .format(txt, rever, colors['limpo'], colors['amar'], colors['azul']))
else:
    print('{3}{0}{2} lido de trás para frente é {4}{1}{2}, portanto não é um palindromo!'
          .format(txt, rever, colors['limpo'], colors['amar'], colors['azul']))
