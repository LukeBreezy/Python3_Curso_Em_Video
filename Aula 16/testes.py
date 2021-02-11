print("=== DESAFIO LUCAS / YAN ===")

n = str(input("Digite seu nome completo: ")).strip()
nome = n.split()

if len(nome) == 1:
    print("Seu nome é muito curto!")
else:
    print("Composto por {} nomes.".format(len(nome)))

teste = nome.count('de')

print(teste)



print("O maior nome é o {}".format(min(nome)))
print("O menor nome é o {}".format(max(nome)))


