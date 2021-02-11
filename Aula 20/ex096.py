def area(larg, comp):
    a = larg * comp
    print(f'Um terreno {larg:.1f}x{comp:.1f}, tem a área de {a:.1f}m²')


# Main
print('ÁREA DO TERRENO')
area(larg=float(input('Largura em metros: ')), comp=float(input('Comprimento em metros: ')))
