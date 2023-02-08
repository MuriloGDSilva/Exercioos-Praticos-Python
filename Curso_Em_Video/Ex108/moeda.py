# Adapte o código do desafio #107, criando uma função adicional chamada moeda()
#que consiga mostrar os números como um valor monetário formatado.

def aumentar(preco=0):
    res = preco + (preco * 10/100)
    return res


def diminuir(preco=0):
    res = preco - (preco * 10/100)
    return res


def dobro(preco=0):
    res = preco * 2
    return res


def metade(preco=0):
    res = preco / 2
    return res

def moeda(preco=0,par='R$'):
    return f'{par}{preco:.2f}'.replace(".",",")