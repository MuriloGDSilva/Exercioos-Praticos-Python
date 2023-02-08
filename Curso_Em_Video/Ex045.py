#Crie um programa que faça o computador jogar Jokenpô com você.

#jOGADAS
from time import sleep
import emoji
itens = [emoji.emojize(':raised_fist:'), emoji.emojize(':raised_hand:'), emoji.emojize(':victory_hand:')]

#jOGADA DO COMPUTADOR
from random import randint
jogada_computador = randint(0,2)
#Titulo
titulo = 'Vamos jogar jokenpo'
# Opçoes de jogada
print('='*50)
print(titulo.center(50))
print('='*50)
sleep(0.5)
print('''Escolha sua jogada
[0] Pedra
[1] Papel
[2] Tesoura''')
#Escolha do usuario
jogada_usuario = int(input('Escoha uma das opçõs acima: ').title())
if jogada_usuario >=3:
    print('Jogada inválida'.upper())
    exit()
elif jogada_usuario < 0:
    print('Jogada inválida'.upper())
    exit()
print('jo'.upper())
sleep(0.75)
print('ken'.upper())
sleep(0.75)
print('po'.upper())

print('='*30)

sleep(1)
#Jogadas do computador & usuario
print(f'Jogada do computador: {itens[jogada_computador]}\nsua jogada: {itens[jogada_usuario]}'.title())

#Comparaçao das jogadas
    #pedra
if jogada_usuario == 0:
    if jogada_computador == 0:
        print('Empate!'.upper())
    elif jogada_computador == 1:
        print('VocÊ Perdeu, Tente novamente!!!'.upper())
    elif jogada_computador == 2:
        print('VocÊ Ganhou!! Parabéns!!'.title())

    #Papel
elif jogada_usuario == 1:
    if jogada_computador == 0:
        print('VocÊ Ganhou!! , Parabéns!!!'.title())
    elif jogada_computador == 1:
        print('Empate!'.upper())
    elif jogada_computador == 2:
        print('VocÊ Perdeu, Tente novamente!!'.upper())

    #Tesoura
elif jogada_usuario == 2:
    if jogada_computador == 0:
        print('VocÊ Perdeu, Tente novamente!!'.upper())
    elif jogada_computador == 1:
        print('VocÊ Ganhou!!, Parabéns!!'.title())
    elif jogada_computador == 2:
        print('Empate!'.upper())
