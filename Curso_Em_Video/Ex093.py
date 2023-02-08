#Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
dados_jogador = dict()
dados_jogador['nome'] = input('Nome do jogador: ')
dados_jogador['qtd_partidas'] = int(input('Total de paridas jogadas: '))
partidas = list()
for c in range(1,dados_jogador['qtd_partidas'] + 1):
    partidas.append(int(input(f'Quantidade de GOLS na {c}° partida: ')))

dados_jogador['Gol_por_partida'] = partidas
dados_jogador['tot_Gols'] = sum(partidas)
print('_-'*45)
print(dados_jogador)
print('_-'*45)
for k , v in dados_jogador.items():
    print(f'O campo: {k} tem valor: {v}')
print('_-'*45)
print(f'O jogador {dados_jogador["nome"]} jogou um total de {dados_jogador["qtd_partidas"]} partidas: ')
for i , v in enumerate(partidas):
    print(f'  {i + 1}° PARTIDA {v} GOLS. ')
print(f'Total de gols: {dados_jogador["tot_Gols"]}')
