#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
lista_numeros = []
for c in range (1,6):
    numeros =(int(input(f'Digite o {c}º Número: ')))
    lista_numeros.append(numeros)
print(f'O maior valor digitado foi: {max(lista_numeros)} na posição:',end='')
for indice , numero in enumerate(lista_numeros):
    if numero == max(lista_numeros):
        print(f'{indice + 1}',end=',')
print(f'\nO menor número digitado foi: {min(lista_numeros)} na posição: ',end='')
for indice , numero in enumerate(lista_numeros):
    if numero == min(lista_numeros):
        print(f'{indice + 1} ',end=',')