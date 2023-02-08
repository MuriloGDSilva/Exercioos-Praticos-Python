#Faça um programa que leia um numero inteiro qualquer e mostre na tela  sua tabuada
print('=====Calculando a tabuada====='.upper())
numero = int(input('Digite um número: '))
for numero2 in range(1,11):
    resultado = numero * numero2
    print(f'{numero} X {numero2} = {resultado}')
print('='* 20)