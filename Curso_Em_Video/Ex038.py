#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#- O primeiro valor é maior
#- O segundo valor é maior
#- Não existe valor maior, os dois são iguais
from time import sleep
import random
print('=-'*10)
print('Gerando números'.upper())
print('-='*10)

sleep(3)
numero_1 = random.randint(1,100)
numero_2 = random.randint(1,100)
print(f'Comparando os Números {numero_1} & {numero_2}....'.upper())
sleep(3)
if numero_1 > numero_2:
    print('O primeiro numero é maior!!')
elif numero_1 < numero_2:
    print('O segundo numero é maior!!')
elif numero_1 == numero_2:
    print('Não existe valor maor entre os número, Os dois são iguais!!')