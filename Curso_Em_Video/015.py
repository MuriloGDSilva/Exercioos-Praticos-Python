# Escreva um programa que pergunte a quantidade de Km percorridos por um  carro alugado e a qauntidade de dias pelos
#quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado

carro = float(input('Digite a quantidade de dias que você ficou com o carro: '))
km = float(input('Digite quantos Km´s foram percorrridos com o carro '))
preço = carro * 60 + km * 0.15
print(f'Você ficou {carro} dias com o carro e {km}Km´s foram percorridos\n------CALCULANDO VALOR APAGAR------')
print(f'Valor total a pagar {preço}')
print('- ' * 45)