# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
numeros_dvisiveies = 0
usuario = int(input('Digite um número: '))
for n in range(1,usuario + 1):
    if usuario % n == 0:
        print(f'\033[32m{n}\033[m',end=' -> ')
        numeros_dvisiveies +=1
    else:
        print(f'\033[31m{n}\033[m',end=' -> ')
if numeros_dvisiveies > 2:
    print(f'O número: {usuario} é divisel por {numeros_dvisiveies} números \nou seja ele não é um número primo.')
elif numeros_dvisiveies <= 2:
    print(f'O número: {usuario} é divisel por {numeros_dvisiveies} números \nou seja ele é um número primo.')
