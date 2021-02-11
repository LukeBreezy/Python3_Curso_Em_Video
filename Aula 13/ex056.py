pessoas = []    # pessoas = [[nome, idade, sexo]]
media = 0       # Média de idade de pessoas cadastradas
h_m_v = 0       # Indice na lista pessoas que contem o homem mais velho
m_m_20 = 0      # Quantidade de mulheres com menos de 20 anos

for i in range(0, 4):
    # Inserindo nome, idade e sexo das pessoas
    print('===== {}ª pessoa ====='.format(i+1))
    pessoas.append([])
    pessoas[i].append(str(input('Nome: ')))
    pessoas[i].append(int(input('Idade: ')))
    pessoas[i].append(str(input('Sexo[M/F]: ')).upper())

    # Preparando a variável para o calculo da média
    media += pessoas[i][1]

    # Identificando o homem mais velho
    if pessoas[i][2] == 'M' and pessoas[i][1] > pessoas[h_m_v][1]:
        h_m_v = i

    # Contando quantas mulheres tem menos de 20 anos
    if pessoas[i][2] == 'F' and pessoas[i][1] < 20:
        m_m_20 += 1

# Exibindo algumas informações

# Média
media /= len(pessoas)
print('A média de idade do grupo é de {} anos'.format(round(media)))

# Homem mais velho
print('Não há homens cadastrados!' if h_m_v == 0 and pessoas[h_m_v][2] != 'M'
      else 'O homem mais velho é {}!'.format(pessoas[h_m_v][0]))

# Quantidade de mulheres com menos de 20 anos de idade
print('Existe {} mulher com menos de 20 anos'.format(m_m_20) if m_m_20 == 1
      else 'Existem {} mulheres com menos de 20 anos'.format(m_m_20))
