pessoas = {
    'nome': [],
    'idade': [],
    'sexo': []
}

h_m_v = 0       # Indice na lista pessoas que contem o homem mais velho
m_m_20 = 0      # Quantidade de mulheres com menos de 20 anos

for i in range(0, 4):
    # Inserindo nome, idade e sexo das pessoas
    print('===== {}ª Pessoa ====='.format(i+1))
    pessoas['nome'].append(str(input('Nome: ')))
    pessoas['idade'].append(int(input('Idade: ')))
    pessoas['sexo'].append(str(input('Sexo: ')))

    # Identificando o homem mais velho
    if pessoas['sexo'][i] == 'M' and pessoas['idade'][i] > pessoas['idade'][h_m_v]:
        h_m_v = i

    # Contando quantas mulheres tem menos de 20 anos
    if pessoas['sexo'][i] == 'F' and pessoas['idade'][i] < 20:
        m_m_20 += 1

# EXIBINDO ALGUMAS INFORMAÇÕES

# Média
media = sum(pessoas['idade']) / len(pessoas['idade'])    # Calculando a média de idade do grupo
print('A média de idade do grupo é de {} anos.'.format(round(media)))

# Homem mais velho
print('Não há homens cadastrados!' if h_m_v == 0 and pessoas['sexo'][h_m_v] != 'M'
      else 'O homem mais velho é {}.'.format(pessoas['nome'][h_m_v]))

# Quantidade de mulheres com menos de 20 anos de idade
print(('Existe {} mulher com menos de 20 anos.'.format(m_m_20) if m_m_20 == 1
       else 'Existem {} mulheres com menos de 20 anos.'.format(m_m_20)
       )
      if m_m_20 > 0 else 'Não existem mulheres cadastradas!')
