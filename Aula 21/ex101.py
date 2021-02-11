# =-=-=-=  FUNÇÕES  =-=-=-=
def voto(nasc_dt):
    """
    A função informa se o voto da pessoa é obrigatório, opcional ou se não vota.
    :param nasc_dt: Recebe a data de nascimento do eleitor.
    :return: print()
    """
    from datetime import datetime
    dt_atual = datetime.now().year
    idade = dt_atual - nasc_dt

    if idade < 16:
        print(f'Com {idade} anos de idade: NÃO VOTA.')
    elif 16 <= idade < 18 or idade > 65:
        print(f'Com {idade} anos de idade: VOTO OPCIONAL.')
    else:
        print(f'Com {idade} anos de idade: VOTO OBRIGATÓRIO.')


# =-=-=-=  MAIN  =-=-=-=
nasc = int(input('Digite o ano do nascimento: '))
voto(nasc)
