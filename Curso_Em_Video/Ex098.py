#Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

def contador(i=0,f=0,p=0):
    print('Contador de 1 a 10: ')
    for c in range(1,11):
        print(f'{c} => ',end='')
    print('fim')
    print('Contador de 10 a 0 vontando de 2')
    for c in range(10,-1,-2):
        print(f'{c} => ',end='')
    print('fim')
    print('Contador personalizado: ')
    for c in range(i,f+1,p):
        print(f'{c} => ',end='')
    print('fim')

inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio,fim,passo)