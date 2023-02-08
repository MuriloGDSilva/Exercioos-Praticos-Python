# Escreva um programa que leia um numero real qualquer pelo teclado e mostre na tela sua porçao inteira.
# Exemplo : Digite um numero: 6.127, O numero 6.127 tem a parte inteira 6.
from math import trunc
numero_real = float(input('Digite  numero real: '))
print(f'Seu número: --->{numero_real}<---\nParte inteira dele: {trunc(numero_real)}')