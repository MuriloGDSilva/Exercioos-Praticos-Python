#Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
from time import sleep

def sortear(num = 0):
    num_sorteado = randint(1,100)
    return num_sorteado

v = 0
d = 0
print('-'*40)
print('Vamos Jogar'.center(40))
print('-'*40)

while d == 0:
    numero_aleatorio = sortear()
    usuario = input('Escolha par ou impar: ').title().strip()
    print('Gerando Número....')
    sleep(0.50)
    print('-' * 40)
    print(f'Número sorteado: {numero_aleatorio}')

    if usuario in 'Par':
        if numero_aleatorio % 2 == 0:
            print('Par')
            v += 1
            print('Voce Ganhou!!')
            print('-' * 40)

        else:
            print('Impar')
            d += 1
            print('Voce Perdeu, Tente Novamente')
            print('-' * 40)

    elif usuario in 'Impar':
        if numero_aleatorio % 2 == 0:
            print('Par')
            d += 1
            print('Voce Perdeu, Tente Novamente')
            print('-' * 40)

        else:
            print('Impar')
            v += 1
            print('Voce Ganhou!!')
            print('-'*40)

print(f'Total de vitorias consecutivas: {v}')