from time import sleep

colors = {
    'limpo': '\033[m',
    'casa': '\033[1;35m',
    'salario': '\033[1;34m',
    'anos': '\033[1;30m',
    'mensal': '\033[1;36m',
    'sal30': '\033[1;32m',
    'aprovado': '\033[36m',
    'desaprovado': '\033[31m'
}

print('''Para verificar a aprovação do financiamento da casa,
preencha as informações abaixo.''')
vlr_casa = float(input('Digite o valor da \033[35mcasa\033[0m: R$'))
salario = float(input('Digite o valor do seu \033[34msalário\033[0m: R$'))
anos = int(input('Em quantos \033[30manos\033[0m pretende pagar a \033[35mcasa\033[0m? '))

print('''
Para que o financiamento da {}casa{} seja aprovado, 
o valor da {}mensalidade{} não poderá ultrapassar 
30% do valor do seu {}salário{}!

{}Processando...'''.format(colors['casa'], colors['limpo'], colors['mensal'], colors['limpo'],
                           colors['salario'], colors['limpo'], '\033[033m'), colors['limpo'])

sleep(4.5)
mensal = vlr_casa / (anos * 12)
salario30 = salario * 0.3

if salario30 < mensal:
    colors['sal30'] = '\033[31m'

print('''
Valor da {}casa{}: R${:.2f}
{}Mensalidade{}: R${:.2f}
{}Salário{}: R${:.2f}
{}Salário{} 30%: {}R${:.2f}{}
Prazo: {} {}Anos{}
'''.format(colors['casa'], colors['limpo'], vlr_casa,
           colors['mensal'], colors['limpo'], mensal,
           colors['salario'], colors['limpo'], salario,
           colors['salario'], colors['limpo'], colors['sal30'], salario30, colors['limpo'],
           anos, colors['anos'], colors['limpo']))

if salario30 > mensal:
    print('{}Parabéns, você conseguiu a aprovação para o financiamento!'.format(colors['aprovado']))
elif salario30 < mensal:
    print('{}Sentimos muito, mas infelizmente você não conseguiu a aprovação!'.format(colors['desaprovado']))
