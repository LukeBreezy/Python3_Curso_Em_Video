from datetime import date

ano_atual = date.today().year

infos = dict()

infos['nome'] = input('Nome: ')
infos['idade'] = ano_atual - int(input('Ano de nascimento: '))
infos['ctps'] = input('Nº CTPS (0 não tem): ')

if int(infos['ctps']) != 0:
    infos['aposen'] = int(input('Ano de contratação: ')) + 35 - ano_atual + infos['idade']
    infos['salario'] = float(input('Salário: '))

print('=-=-= Informações =-=-=')

for k, v in infos.items():
    print(f'{k.capitalize()}: {v}')


