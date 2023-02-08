#Crie um código em Python que teste se o site da sua escolha está acessível pelo computador usado.
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://github.com/')
except Exception as error:
    print(f'O site não esta disponivel')
    print(error)
else:
    print(f'Consegui acessar o site com sucesso!!')
