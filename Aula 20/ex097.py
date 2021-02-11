# Função para a linha adaptável
def linha(x):
    print('-' * (len(x) + 4))


# Função para exibir o conteúdo com linhas adaptáveis delimitando
def escreva(txt):
    linha(txt)
    print(f'{txt:^{len(txt)+4}}')
    linha(txt)


escreva('Lucas')
escreva('Luke Breezy')
escreva('Indigo')
