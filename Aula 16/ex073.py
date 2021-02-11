equipes = ('Los Angeles Lakers', 'LA Clippers', 'Denver Nuggets', 'Houston Rockets',
           'Oklahoma City Thunder', 'Utah Jazz', 'Dallas Mavericks', 'Portland Trail Blazers',
           'Memphis Grizzlies', 'Phoenix Suns', 'San Antonio Spurs', 'Sacramento Kings',
           'New Orleans Pelicans', 'Minnesota Timberwolves', 'Golden State Warriors')

print(f'\033[1;33m{" NBA ":=^17}')
print('\033[0m=~'*8)

# 5 Primeiros
print('\n\033[1;4;39m5 PRIMEIROS COLOCADOS\033[0m')
for i in range(0, 5):
    print(f'{i+1}º - {equipes[i]}')

print('=~'*8)
# 4 Ultimos
print('\n\033[1;4;39m4 ULTIMOS COLOCADOS\033[0m')
for i in range(-4, 0):
    print(f'{len(equipes) + i+1}º - {equipes[i]}')

print('=~'*8)
# Ordem Alfabetica
print('\n\033[1;4;39mLISTA EM ORDEM ALFABETICA\033[0m')
for i in sorted(equipes):
    print(i)

print('=~'*8)
# Exibindo a posição do Utah Jazz
print('\n\033[1;4;39mCOLOCAÇÃO DO UTAH JAZZ\033[0m')
print(f'Utah Jazz está em {equipes.index("Utah Jazz")}º na colocação.')
