#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numero = int(input("Digite um Número: "))
print('_' * 20)
if numero % 2 == 0:
    print('O número digitado é: PAR')
else:
    print('O número digitado é: ÍMPAR')
print('_' * 20)
