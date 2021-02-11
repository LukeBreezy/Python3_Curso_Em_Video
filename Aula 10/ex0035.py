retas = []

print('Digite o cumprimento de 3 retas(em cm), e veja se é possível formar um triangulo!')

for i in range(0, 3):
    retas.append(float(input('Digite o cumprimento da {}ª reta: '.format(i+1))))

if (retas[0] + retas[1] > retas[2]) and (retas[0] + retas[2] > retas[1]) and (retas[1] + retas[2] > retas[0]):
    print('É possível formar um triangulo com as retas de {}cm, {}cm e {}cm'.format(retas[0], retas[1], retas[2]))
else:
    print('Não é possível formar um triangulo com as retas de {}cm, {}cm e {}cm'.format(retas[0], retas[1], retas[2]))
