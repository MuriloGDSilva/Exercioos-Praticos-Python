#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos_precos = ('Placa-mãe',1.200,'Processador',850,'Memoria-Ram',400,'Placa-Video',2.500)
for item in range(0,len(produtos_precos)):
    if item % 2 == 0:
        print(f'{produtos_precos[item]:.<30}',end='')
    else:
        print(f'R${produtos_precos[item]:>4.3f}')
