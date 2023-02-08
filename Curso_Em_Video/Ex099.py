#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(list):
    return max(list)

lista = list()
while True:
    try:
        usuario = int(input('Digite um número: '))
    except(TypeError,ValueError):
        print('Insira somente números')
        continue
    lista.append(usuario)
    escolha = input('Continuar ?: ').strip().upper()[0]
    if escolha in 'N':
        break
    elif escolha in 'S':
        pass
    else:
        print('Responda apenas com Sim ou Não.')
        escolha = input('Continuar ?: ').strip().upper()[0]

print(f'O maior número: {maior(lista)}')