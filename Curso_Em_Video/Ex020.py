# O mesmo professor do desafio anterior quer sortear a ordem da apresentaçao de trabalhos dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

from random import sample

lista_alunos = list()
for aluno in range(0,4):
    usuario = input('Nome Do Aluno: ')
    lista_alunos.append(usuario)
lista_sorteada = sample(lista_alunos,k=4)
print('_'*30)
print('Lista dos alunos sorteados: ',end=' ')
for a in lista_sorteada:
    print(a,end=', ')