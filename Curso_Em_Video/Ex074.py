#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso,
# mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.


from random import randint
from time import sleep

numeros_aleatorios = (randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100))
print(f'GERANDO NÚMEROS.....')
for digito in numeros_aleatorios:
    print(f'{digito}',end=' => ')
    sleep(0.5)
print(f'\nMaior número gerado: {max(numeros_aleatorios)}\nMenor número gerado: {min(numeros_aleatorios)}')
