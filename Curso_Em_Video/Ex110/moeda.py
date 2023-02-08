#Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(),
#que mostre na tela algumas informações geradas pelas funções que
# já temos no módulo criado até aqui.

def aumentar(preco=0,taxa=0,fat = False):
    res = int(preco + (preco * taxa/100))
    if fat == True:
        return moeda(res)
    else:
        return float(res)


def diminuir(preco=0,taxa=0,fat=False):
    res = int(preco - (preco * taxa/100))
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
    return f'{par} {preco:.2f}'.replace(".",",")


def resumo(p=0,taxa_a=0,taxa_b=0):
    print('-'*30)
    print(f'{"Resumo do Valor":^30}'.upper())
    print('-'*30)
    print(f'Valor Analisado:\t{moeda(p)}')
    print(f'Dobro do preço:\t\t{dobro(p,True)}')
    print(f'Metade do preço:\t{metade(p,True)}')
    print(f'{taxa_a}% de aumento:\t\t{aumentar(p,taxa_a,fat=True)}')
    print(f'{taxa_b}% de redução:\t\t{diminuir(p,taxa_b,fat=True)}')
    print('-'*30)
