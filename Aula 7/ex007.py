def media(x, y):
    if x.isdecimal() is False or y.isdecimal() is False:
        print('Para as notas só servem caracteres numéricos.\nFaça as correções necessárias e tente novamente!')
        media(input('Digite a nota de Exatas: '), input('Digite a nota de Humanas: '))
    elif int(x) > 10 or int(y) > 10:
        print('A nota maxima permitida é 10!\nFaça as correções necessárias e tente novamente!')
        media(input('Digite a nota de Exatas: '), input('Digite a nota de Humanas: '))
    elif int(x) < 0 or int(y) < 0:
        print('A nota miníma permitida é 0!\nFaça as correções necessárias e tente novamente!')
        media(input('Digite a nota de Exatas: '), input('Digite a nota de Humanas: '))
    else:
        print('Média: {:.2f}'.format((int(x) + int(y)) / 2))

x = input('Digite a nota de Exatas: ')
y = input('Digite a nota de Humanas: ')

media(x, y)