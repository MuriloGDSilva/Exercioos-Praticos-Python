#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
from datetime import date
print('>>>>>Descobrindo se o ano é bissexto<<<<<'.upper())
ano = int(input('Digite o Ano: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano} é Bissexto')
else:
    print(f'O ano {ano} não é bissexto')
print('-'*30)