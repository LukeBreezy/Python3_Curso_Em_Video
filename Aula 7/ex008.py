def convert(x):
    if x.isdecimal() is False:
        print('Insira um valor que represente a quantidade de metros.')
        convert(input('Digite a distância metros: '))
    else:
        km = float(x)/1000
        hm = float(x)/100
        dam = float(x)/10
        dm = float(x)*10
        cm = float(x)*100
        mm = float(x)*1000
        print('{} m é equivalente a:'.format(x))
        print('{} km \n{} hm \n{} dam \n{} dm \n{} cm \n{} mm'.format(km, hm, dam, dm, cm, mm))


medida = str(input('Digite a quantidade de metros: '))
convert(medida)
