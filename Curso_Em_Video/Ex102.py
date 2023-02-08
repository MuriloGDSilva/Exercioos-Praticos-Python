#Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e
# outro chamado show, que será um valor lógico (opcional)
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial.


def fatorial(n,show=False):
    '''
    -Calculo de Fatorial
    :param n: Recebe Numero inteiro para calcular seu fatorial
    :param show: Mostra o processo de calculo do fatorila do n
    :return: Retorna o valor de f
    '''
    f=1
    for c in range(n,0,-1):
        if show == True:
            print(c,end=' ')
            if c > 1:
                print(f'X',end=' ')
            else:
                print(f'=',end=' ')
        f *= c
    return f
print(fatorial(5,True))