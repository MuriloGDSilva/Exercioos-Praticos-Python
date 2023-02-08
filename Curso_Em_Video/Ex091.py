#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter
dados = {'jogador1': randint(1,6),'jogador2': randint(1,6),
         'jogador3': randint(1,6),'jogador4': randint(1,6)}
rankin = list()
print(f'{"JOGADAS":/^20}')
for k , v in dados.items():
    print(f'O {k} tirou : {v}')
    sleep(0.50)
print('-_'*20)
rankin = sorted(dados.items(), key=itemgetter(1), reverse= True)
for i , r in enumerate(rankin):
    print(f'    {i + 1}° LUGAR: {r[0]}: {r[1]}')
print('_-'*20)
