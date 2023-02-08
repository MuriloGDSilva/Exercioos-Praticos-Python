#Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista_numeros = list()
while True:
    lista_numeros.append(int(input('Digite um número: ')))
    escolha = input(f'{"Sim / Não:":>15}').upper()[0]
    while escolha not in 'SN':
        escolha = input(f'{"Sim / Não:":>15}' ).upper()[0]
    if escolha in 'N':
        break
print(f'Foram digitados {len(lista_numeros)} Números.')
if 5 in lista_numeros:
    print(f'o valor 5 foi digitado na posição {lista_numeros.index(5) + 1}')
else:
    print(f'O número 5 não foi digitado.')
lista_numeros.sort(reverse=True)
print(f'Lista dos números decresente:{lista_numeros}')
