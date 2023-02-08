#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule e peça o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R#0,45 para viagens mais longas.

def valor_passagem(distancia):
    '''
    -> Fução para calcular o valor da passagem
    :param distancia: Recebe a distancia da viagem
    :return: Retorno o valor da passagem
    '''
    if distancia > 200:
        preco_passagem = distancia * 0.45
        return preco_passagem
    else:
        preco_passgem = distancia * 0.50
        return preco_passgem

distancia_viagem = float(input('Insira a distancia da sua viagem: '))
print(f'Sua passagem ficará no valor de R${valor_passagem(distancia_viagem)} por pessoa.')

help(valor_passagem)