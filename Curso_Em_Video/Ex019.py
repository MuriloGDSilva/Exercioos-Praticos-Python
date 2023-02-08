# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajuda ele lendo o nome deles e escolhendo e escrevendo o nome.
import random
from random import choice
from time import sleep
lista_alunos = list()
for aluno in range(1,5):
    usuario = str(input(f'Digite o nome do {aluno}°Aluno: ')).strip()
    lista_alunos.append(usuario)

aluno_sorteado = random.choice(lista_alunos)
print(f'Escolhendo aluno.....')
sleep(0.65)
print(f'Aluno sorteado: {choice(lista_alunos)}')