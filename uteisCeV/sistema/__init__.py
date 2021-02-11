def sisCad():
    from uteisCeV.perfumaria import linha
    from uteisCeV.cores import cor

    opt = menu()
    if opt == 1:
        exibeCad()
    elif opt == 2:
        cadastrar()
    elif opt == 3:
        linha(40)
        print(cor('Obrigado por usar o sistema.\nVolte sempre!', 'amar'))
        exit()


def exibeCad():
    from uteisCeV.perfumaria import msg
    from uteisCeV.cores import cor

    msg('PESSOAS CADASTRADAS', tam_c=40)

    try:
        file = open('CADASTROS.txt', 'rt')

    except FileNotFoundError:
        print(cor('Não existem cadastros!', 'cian'))

    else:
        for i in file.readlines():
            nome = i.split(';')[0]
            idade = i.split(';')[1].replace('\n', '')
            print(f'{nome}{idade:>{35 - len(nome)}} anos')
#        print(file.readlines())

    finally:
        sisCad()


def cadastrar():
    from uteisCeV.perfumaria import msg
    from uteisCeV.valida import leiaStr, leiaInt
    from uteisCeV.cores import cor

    msg('NOVO CADASTRO', tam_c=40)
    nome = leiaStr('Nome: ')
    idade = leiaInt('Idade: ')

    try:
        file = open('CADASTROS.txt', 'x')

    except FileExistsError:
        pass

    finally:
        file = open('CADASTROS.txt', 'at')
        file.write(f'{nome};{idade}\n')
        file.close()
        print(cor('Cadastro realizado com sucesso.', 'verd'))
        sisCad()


def menu():
    from uteisCeV.valida import leiaInt
    from uteisCeV.perfumaria import msg, linha
    from uteisCeV.cores import cor

    msg('SISTEMA DE CADASTRO', tam_c=40)

    print(f"{cor('1', 'amar')} - {cor('Ver pessoas cadastradas', 'azul')}")
    print(f"{cor('2', 'amar')} - {cor('Cadastrar pessoa', 'azul')}")
    print(f"{cor('3', 'amar')} - {cor('Sair do sistema', 'azul')}")
    linha(40)

    opt = 0
    while True:
        opt = leiaInt(cor('Selecione uma opção: ', 'cinz'))

        if opt not in (1, 2, 3):
            print(cor('Opção inválida!', 'verm'))
            continue
        else:
            return int(opt)
