from EX115.Sistema.menu import *
from time import sleep
cabesalho('Novo Sistema')
while True:
    linha()
    opcoes(['Ver Pessoas Cadastradas', 'Adicionar Nova Pessoa', 'Encerrar Programa'])
    usuario = leiaint('\033[33mEscolha uma opção: \033[m')
    sleep(0.5)
    if usuario == 1:
        cabesalho('Pessoas Cadastradas')
    elif usuario == 2:
        cabesalho('Adicionar Pessoa')
    elif usuario == 3:
        cabesalho('\033[1;32mPrograma Encerrado,Volte Sempre!!\033[m')
        break
    else:
        print('\033[31mOpção inválida\033[m')
        linha()
        sleep(0.5)