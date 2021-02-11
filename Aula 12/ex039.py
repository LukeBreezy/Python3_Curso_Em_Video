from datetime import date

nascimento = int(input('Informe o ano de seu nascumento, e veja se já está na hora de se alistar: '))
ano_atual = date.today().year
idade = ano_atual - nascimento

if idade < 18:
    print('Faltam {} anos para você se alistar!'.format(18 - idade))
elif idade > 18:
    print('Você deveria ter se alistado a {} atrás!'.format(idade - 18))
else:
    print('Está na hora de se alistar!')

