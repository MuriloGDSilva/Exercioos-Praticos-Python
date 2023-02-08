# Faça um programa que leia algo pelo teclado e mostra na tela seu tipo primitivo,
#  e todas as informaçoes possiveis sobre ele.

frase = input('Digite algo: ')
frase.isalnum()
frase.isalpha()
frase.isnumeric()
frase.isspace()
print(f'Oque voce digitou é:'
      f'{frase.isalnum()}'
      f'{frase.isalpha()}'
      f'{frase.isnumeric()}'
      f'{frase.isspace()}')
