#Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.

compras = list()
tot_compras = 0
acima_mil = 0
contador = 0
mais_barato = 0
nome_barato = ''
while True:
    nome_produto = str(input('Nome do Produto: ')).title()
    valor_produto = float(input('Valor Produto: '))
    if valor_produto >= 1000:
        acima_mil += 1
    tot_compras += valor_produto
    compras.append([nome_produto,valor_produto])
    continuar = input('Continuar comprando ?: Sim/Não]: ').upper().strip()[0]
    if continuar in 'N':
        break
print('-'*30)
print('Lista De Compras'.center(30))
print('-'*30)
for item in compras:
    print(f'{item[0]:<10}\t\t{"R$":>10}{item[1]}')
print('-'*30)
print(f'{"Total:":<10}\t\t{"R$":>10}{tot_compras:.2f}')
print(f'{"Total de produtos acima de Mil Reais: "} {acima_mil}')
for i in compras:
    if contador == 0:
        mais_barato = i[1]
        nome_barato = i[0]
        contador += 1
    else:
        if i[1] < mais_barato:
            mais_barato = i[1]
            nome_barato = i[0]
print(f'{"Produto mais Barato"}: {nome_barato}.')
print('-'*30)