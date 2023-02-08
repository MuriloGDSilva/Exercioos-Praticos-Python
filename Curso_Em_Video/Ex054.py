#Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
maior_idade = 0
menor_idade = 0
for p in range(1,8):
    print(f'------>{p}°{"Pessoa"}<------')
    nasc = int(input('Data de Nascimento: '))
    idade = date.today().year - nasc
    if idade >= 18:
        maior_idade += 1
    else:
        menor_idade += 1
print('='*30)
print('\033[7m',end='')
print(f'Um total de {maior_idade} pessoas, são maiores de idade.')
print(f'Um total de {menor_idade} pessoas, são menores de idade.')
print('\033[0m',end='')
print('='*30)

