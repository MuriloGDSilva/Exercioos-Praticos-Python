#Faça um programa que leia nome e peso de várias pessoas,guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesada.
# C) Uma listagem com as pessoas mais leves.


pessoas = list()
while True:
    nome = input('Nome: ')
    peso = float(input('Peso: '))
    pessoas.append([nome,peso])
    c = input('Continuar? [Sim/Não]: ').upper().strip()[0]
    if c in 'N':
        break
print(f'Total de pessoas cadastradas: {len(pessoas)}')
mais_Pesadas = []
mais_leves = []
for p in pessoas:
    if p[1] >= 75:
        mais_Pesadas.append(p)
    elif p[1] <=70:
        mais_leves.append(p)
print(f'Pessoas mais pesadas: {mais_Pesadas}')
print(f'Pessoas Mais leves: {mais_leves}')

