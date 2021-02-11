colors = {
    'limpo': '\033[m',
    'roxo': '\033[1;35m',
    'bran': '\033[1;30m',
    'azul': '\033[1;34m',
    'amar': '\033[1;33m',
    'verm': '\033[1;31m'
}

opt = ''
num1 = int(input('Digite um número qualquer: '))
num2 = int(input('Digite outro número qualquer: '))

while opt != 8:
    print('{}=*'.format(colors['limpo']) * 20)
    opt = int(input('{}Selecione uma opção:\n{}'.format(colors['azul'], colors['limpo']) +
                    '[1] Somar\n' +
                    '[2] Subtrair\n' +
                    '[3] Multiplicar\n' +
                    '[4] Dividir\n' +
                    '[5] Maior\n' +
                    '[6] Menor\n' +
                    '[7] Novos números\n' +
                    '[8] Sair\n'
                    ))

    if opt == 1:
        soma = num1 + num2
        print('Você selecionou [1] Soma\n'
              'O resultado é: {}{}'.format(colors['amar'], soma))
    elif opt == 2:
        subt = num1 - num2
        print('Você selecionou [2] Subtração\n'
              'O resultado é: {}{}'.format(colors['amar'], subt))
    elif opt == 3:
        mult = num1 * num2
        print('Você selecionou [3] Multiplicação\n'
              'O resultado é: {}{}'.format(colors['amar'], mult))
    elif opt == 4:
        divs = num1 / num2
        print('Você selecionou [4] Divisão\n'
              'O resultado é: {}{:.2f}'.format(colors['amar'], divs))
    elif opt == 5:
        maior = max(num1, num2)
        print('Você selecionou [5] Maior\n'
              'O resultado é: {}{}'.format(colors['amar'], maior))
    elif opt == 6:
        menor = min(num1, num2)
        print('Você selecionou [6] Menor\n'
              'O resultado é: {}{}'.format(colors['amar'], menor))
    elif opt == 7:
        print('Você selecionou [7] Novos números\n')
        num1 = int(input('Digite um número qualquer: '))
        num2 = int(input('Digite outro número qualquer: '))
    elif opt == 8:
        print('Você selecionou [8] Sair\n'
              'Obrigado por utilizar o nosso sistema, até mais!')
    else:
        print('\033[31mOpção inválida, tente novamente!')
        continue
