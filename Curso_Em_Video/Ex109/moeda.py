#Modifique as funções que foram criadas no desafio 107
# para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou
# não formatado pela função moeda(), desenvolvida no desafio 108.

def aumentar(preco=0,fat = False):
    res = int(preco + (preco * 10/100))
    if fat == True:
        return moeda(res)
    else:
        return float(res)


def diminuir(preco=0,fat=False):
    res = int(preco - (preco * 10/100))
    if fat == True:
        return moeda(res)
    else:
        return float(res)


def dobro(preco=0,fat=False):
    res = preco * 2
    if fat == True:
        return moeda(res)
    else:
        return float(res)


def metade(preco=0,fat=False):
    res = int(preco / 2)
    if fat == True:
        return moeda(res)
    else:
        return float(res)


def moeda(preco = 0 ,par='R$'):
    return f'{par}{preco:.2f}'.replace(".",",")