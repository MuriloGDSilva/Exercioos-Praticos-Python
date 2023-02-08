#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

from random import randint
numero_computador = randint(1,10)
total_palpite = 0
acertou = False
while acertou == False:
    numero_usuario = int(input('Advinhe o número de 1 a 10: '))
    total_palpite = total_palpite + 1
    if numero_usuario == numero_computador:
        acertou = True
    else:
        if numero_usuario > numero_computador:
            print('Menor ')
        elif numero_usuario < numero_computador:
            print('Maior')

print(f'Voce acertou!! em {total_palpite} vezes')