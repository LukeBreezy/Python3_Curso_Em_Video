infos = {  # infos vai armazenar as informações que o usuário inserir
    'idade': [],
    'sexo': []
}

# Abaixo variáveis que carregarão quantidades de:
# pessoas com mais de 18 anos; homens; mulheres com mais de 20 anos respectivamente.
maior_18 = qtde_h = m_menos_20 = 0

continuar = True

print('Cadastre idade e sexo de quantas pessoas quiser e no final veja algumas informações.')
print('~='*20)
while continuar:
    infos['idade'].append(int(input('Idade: ')))
    infos['sexo'].append(input('Sexo [M / F]: ').upper())

    aux = len(infos['idade']) - 1       # Variável auxiliar, para guardar a quantidade de pessoas cadastradas

    while infos['sexo'][aux] not in 'MF':
        infos['sexo'][aux] = input('Sexo [M / F]: ').upper()


    if infos['idade'][aux] > 18:        # Incrementando a quantidade de pessoas com mais de 18 anos
        maior_18 += 1

    if infos['idade'][aux] < 20 and infos['sexo'][aux] == 'F':      # Incrementando a quantidade de mulheres com menos de 20 anos
        m_menos_20 += 1

    continuar = bool(int(input('Quer continuar? [1 - Sim / 0 - Não]: ')))   # Opção de continuar ou parar

    print('~='*20)

qtde_h = infos['sexo'].count('M')

print(f'''
Pessoas com mais de 18 anos: {maior_18}
Quantidade de homens: {qtde_h}
Mulheres com menos de 20 anos: {m_menos_20}
''')
