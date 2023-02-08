# Crie um Programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.
# Considere que US$~1,00 = R$~5,21
import math
carteira = float(input('Insira o valor que deseja trocar: '))
print(f'Valor inserido: R${carteira}\nValor convertido em Dólar: U${math.ceil(carteira / 5.21)}')