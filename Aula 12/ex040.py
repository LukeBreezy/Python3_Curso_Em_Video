print('Digite as notas do aluno para ver se ele foi aprovado!')

notas = [float(input('Digite a primeira nota: ')),
         float(input('Digite a segunda nota: '))]

media = float(sum(notas) / 2)

print(media)

if media >= 7:
    print('\033[1;36mAprovado')
elif 5 <= media <= 6.9:
    print('\033[1;33mRecuperação')
else:
    print('\033[1;31mReprovado')
