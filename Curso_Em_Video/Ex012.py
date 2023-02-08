#Faça um algoritimo que leia o preço de um produto e mostra seu novo preço, com 5% de Desconto.

produto = float(input('Digite o valor do produto: '))
print(f'Valor original R${produto}\nValor do desconto R${produto * 0.05}\nValor com desconto R${produto * 0.95}')