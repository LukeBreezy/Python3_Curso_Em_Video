num = int(input('Digite um número e veja se ele é primo: '))
div = 2

print("(O número {} é divisível pelos valores em amarelo)")

for i in range(1, num+1):
    if num != i != 1:
        if num % i == 0:
            div += 1
            print("\033[33m {} \033[0m".format(i), end='')
        else:
            print("\033[34m {} \033[0m".format(i), end='')
    elif i == num or i == 1:
        print("\033[33m {} \033[0m".format(i), end='')

print("\n")
print("\n")

if div == 2:
    print("O número {} só é divisível por 1 e por ele memso, portanto é primo!".format(num, div))
elif num == 1:
    print("O número 1 só é divisível por ele mesmo, portanto não é primo!")
else:
    print("O número {} é divisível por {} números, portanto não é primo!".format(num, div))
