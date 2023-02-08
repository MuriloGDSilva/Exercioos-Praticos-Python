#Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média
dados = dict()
lista_pessoas = list()
idade_media = 0
while True:
    dados.clear()
    dados['Nome'] = input('Nome: ')
    dados['Sexo'] = input('Sexo [M/F] ').upper()[0]
    while dados['Sexo'] not in 'MF':
        dados['Sexo'] = input('Sexo [M/F] ').upper()[0]
    dados['Idade'] = int(input('Idade: '))
    idade_media += dados['Idade']
    lista_pessoas.append(dados.copy())
    escolha = str(input('Adicionar pessoa: [Sim/Não]: ')).upper()[0]
    while escolha not in 'SN':
        escolha = str(input('Adicionar pessoa: [Sim/Não]: ')).upper()[0]
    if escolha in 'Nn':
        break
print(f'{"Pessoas Cadastradas":.^40}')
print(f' Total de pessoas cadastradas: {len(lista_pessoas)}')
print(f'A idade média do grupo é de: {idade_media / len(lista_pessoas):.2f}')
print(f'{"Lista De Mulheres: "}',end='')
for p in lista_pessoas:
    if p['Sexo'] in 'Ff':
        print(f'{p["Nome"]} - {p["Idade"]}',end=' ')
print(f'\n{"Lista das pessoas acima da média".title()}')
for p in lista_pessoas:
    if p['Idade'] >= idade_media / len(lista_pessoas):
        print(f'{p["Nome"]}-{p["Idade"]}',end=' ')
