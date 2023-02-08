#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

 #à vista dinheiro/cheque: 10% de desconto

# à vista no cartão: 5% de desconto

# em até 2x no cartão: preço formal

# 3x ou mais no cartão: 20% de juros

valor_produto = float(input('Insira o valor do produto R$: '))

print('''Essas são suas codições de pagamento:
[1] Ávista dinheiro ou cheque: 10% de desconto
[2] Ávista no cartão: 5% de Desconto
[3] Em até 2x no cartão: preço formal
[4] Em 3x ou mais no cartão: 20% de juros'''.title())
escolha = int(input('Escolha uma opção: '))

if escolha == 1:
    avista = valor_produto - (valor_produto * 10/100)
    print(f'Valor do produto: R${valor_produto}\nValor do produto com desconto: R${avista}')
elif escolha == 2:
    avista_cartao = valor_produto - (valor_produto * 5/100)
    print(f'Valor do produo: {valor_produto}\nValor do produto com desconto: {avista_cartao}')
elif escolha == 3:
    parcela = valor_produto / 2
    print(f'Valor do produto: {valor_produto}\nValor da parcela: {parcela}')
elif escolha == 4:
    parcela_juros = int(input('Em quantas parcelas você desea fazer ?'))
    produto_juros = valor_produto + (valor_produto * 20/100)
    print(f'Valor d produto com juros: {produto_juros}\nValor da parcela com juros: {produto_juros / parcela_juros}')
else:
    print(f'Opção inválida')