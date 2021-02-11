import requests

url = 'http://cursoemvideo.com'

try:
    requests.head(url).status_code

except requests.exceptions.ConnectionError:
    print(f'\033[31mO site "{url}" está indisponivel no momento, tente mais tarde!\033[m')

else:
    print(f'\033[32mO site "{url}" está disponivel!\033[m')

finally:
    print('\nObrigado, volte sempre!')
