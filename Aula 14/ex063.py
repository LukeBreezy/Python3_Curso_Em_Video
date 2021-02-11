print('==== Fibonacci ====')
cont = int(input('Digite a quantidade de termos que quer ver da sequência Fibonacci: '))
fib = []

while len(fib) < cont:
    if len(fib) == 0:
        fib.append(0)
    elif len(fib) == 1:
        fib.append(1)
    else:
        fib.append(fib[len(fib)-1] + fib[len(fib)-2])
    print(fib[len(fib) - 1], end=' | ')

print(fib)
