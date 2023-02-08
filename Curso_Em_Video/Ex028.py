#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e
# peça para o usuário descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usúario venceu ou perdeu.

import random

numero_aleatorio = random.randint(0,5)
errou = False
while errou == False:
    chute = int(input('Chute um número entre 0 & 5: '))
    if chute == numero_aleatorio:
        errou = True
        print('VocÊ Acertou!! PARABÉNS!!!')
    elif chute >= 6:
        print('Numero inválido')
    else:
        print('Você Perdeu!! TENTE OUTRA VEZ!!')
