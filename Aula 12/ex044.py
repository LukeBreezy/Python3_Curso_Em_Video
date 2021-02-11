preco = float(input('Digite o valor do produto: R$'))
cond_pag = int(input('Escolha a forma de pagamento: \n'
                     '1 - À vista em dinheiro / cheque \033[4m(10% de desconto)\033[m\n'
                     '2 - À vista no cartão \033[4m(5% de desconto)\033[m\n'
                     '3 - Parcelado no cartão \033[4m(2x sem juros / 3x ou mais 20% de juros)\033[m\n\n'))

print('Preço normal: \033[1;37mR${:.2f}\033[m'.format(preco))

if cond_pag == 1:
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('Forma de pagamento: \033[1;37mÀ vista em dinheiro / cheque\033[m\n'
          'Desconto: \033[1;37m10%\033[m\n'
          'Preço com desconto: \033[1;37m{:.2f}\033[m'.format(preco * 0.9))

elif cond_pag == 2:
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('Forma de pagamento: \033[1;37mÀ vista no cartão\033[m\n'
          'Desconto: \033[1;37m5%\033[m\n'
          'Preço com desconto: \033[1;37m{:.2f}\033[m'.format(preco * 0.95))

elif cond_pag == 3:
    parcelas = int(input('Em quantas vezes deseja parcelar: '))

    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('Forma de pagamento: \033[1;37mParcelado no cartão\033[m\n'
          'Parcelado em: \033[1;37m{}x\033[m\n'.format(parcelas) +
          'Mensalidade: \033[1;37mR${:.2f}\033[m'.format(preco / parcelas))

    if parcelas == 2:
        print('Juros: \033[1;37m-\033[m\n'
              'Preço com juros: \033[1;37mR${:.2f}\033[m'.format(preco * 1))

    elif parcelas >= 3:
        print('Juros: \033[1;37m20%\033[m\n'
              'Preço com juros: \033[1;37mR${:.2f}\033[m'.format(preco * 1.2))
    else:
        print('Valor para parcelas inválido')

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
