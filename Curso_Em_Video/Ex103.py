#Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome='<Desconhecido>',gols=0):
    print(f'----- Ficha Do Jogador {nome.upper()}-----')
    print(f'O Jogador {nome.title()} Marcou um total de {gols} Gol(s) no campeonato.')
nome_jogador = input('Nome Do Jogador: ')
tot_gols = str(input('Total de Gols no Campeonato: '))
if tot_gols.isnumeric():
    tot_gols = int(tot_gols)
else:
    tot_gols=0

if len(nome_jogador) == 0:
    ficha(gols=tot_gols)
else:
    ficha(nome_jogador,tot_gols)