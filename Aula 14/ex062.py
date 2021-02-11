print('{:=^16}'.format(' PA '))
termo = int(input('Primeiro termo da PA: '))
razao = int(input('Razão da PA: '))
qtd_termos = 10
enesimo = termo + razao * qtd_termos

print('A seguir, os 10 primeiros termos da PA')
while termo < enesimo:
    print(termo, end=' | ')
    termo += razao
    if termo == enesimo:
        print('\nDeseja mostrar mais termos?\nSe sim, digite quantos. Se não, digite 0.')
        enesimo += razao * int(input())
