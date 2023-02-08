# Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogadores = dict()
gol_PARTIDA = list()
lista_jogadores = list()
while True:
    jogadores.clear()
    gol_PARTIDA.clear()
    jogadores['Nome'] = str(input('Nome Do Jogador: '))
    jogadores['Total_Partidas'] = int(input('Total De Partidas Jogadas: '))
    for gol in range(1, jogadores['Total_Partidas'] + 1):
        gol_PARTIDA.append(int(input(f'Total de gols na {gol}° Partida: ')))
    jogadores['Gols_por_partida'] = gol_PARTIDA[:]
    jogadores['Total_Gols'] = sum(gol_PARTIDA)
    lista_jogadores.append(jogadores.copy())
    escolha = str(input('Adicionar Jogador: 1 Sim/2 Não: ')).upper().strip()[0]
    if escolha in 'N':
        break
print('_-' * 25)
print('DETALHAMETO'.center(40))
print('_' * 55)
print(' Id', end=' ')
for k in jogadores.keys():
    print(f'{k:<8}', end=' ')
print()
print('_' * 55)

for e, n in enumerate(lista_jogadores):
    print(f'{e:>3} ', end='')
    for j in n.values():
        print(f'{str(j):<15}', end='')
    print()
print('_' * 55)
