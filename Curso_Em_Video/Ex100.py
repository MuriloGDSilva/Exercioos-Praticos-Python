#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai
# mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint

lista_nums = list()


def sorteia(*num):
    for n in range(0,5):
        num = randint(1,100)
        lista_nums.append(num)
    print(f'Numeros sorteados: {lista_nums}')


def somapar():
    somapar = 0
    for d in lista_nums:
        if d % 2 == 0:
            somapar += d
    print(f' A soma dos números pares é de: {somapar}')



sorteia()
somapar()