from Aula22_Uteis import fatorial, msg

# from <pacote/modulo> import <pacote/modulo/função>
# os modulos tem funções dentro, e os pacotes podem ter pacotes e/ou modulos dentro

# PACOTE > MODULO > FUNÇÃO

num = int(input('Digite um número para ver o fatorial: '))
fat = fatorial(num)

msg(f'O fatorial de {num} é {fat}', 7)


