#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados
# e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

lista_geral = []
lista_de_jogos = []
qtd_jogos = int(input('Qunatos jogos deseja gerar ?: '))
for jogo in range(1,qtd_jogos + 1):
    for n in range(1,7):
        numeros = randint(1,60)
        if numeros not in lista_geral:
            lista_geral.append(numeros)
    lista_de_jogos.append(lista_geral[:])
    lista_geral.clear()
print('-_'* 30)
print(f'{"GERANDO SEUS JOGOS...": ^60}')
print('-_'* 30)
for i , j in enumerate(lista_de_jogos):
    print(f'{i + 1}->{j}')
    print('-'*30)