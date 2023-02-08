#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

aluno = {}
aluno['nome'] = input('Digite o nome do aluno: ')
aluno['media'] = float(input(f'Digite a média do aluno {aluno["nome"]}: '))
if aluno['media'] >= 6:
    aluno['situação'] = 'Aprovado'
else:
    aluno['situação'] = 'Reprovado'
print('-_'*20)
for k , v in aluno.items():
    print(f'{k}: {v}')
print('-_'*20)
