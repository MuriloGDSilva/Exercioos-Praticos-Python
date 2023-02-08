#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o
# usuário possa mostrar as notas de cada aluno individualmente.

lista_geral = []
lista_alunos = []
while True:
    nome = input('Digite o nome do aluno: ').strip().upper()
    lista_geral.append(nome)
    nota_1 = float(input('Digite a 1° Nota: '))
    lista_geral.append(nota_1)
    nota_2 = float(input('Digite a 2° Nota: '))
    lista_geral.append(nota_2)
    media = (nota_1 + nota_2) / 2
    lista_geral.append(media)
    lista_alunos.append(lista_geral[:])
    lista_geral.clear()
    escolha = input('Adicionar Aluno: [s/n]').upper()[0]
    if escolha in 'N':
        break
print('-'*20)
print(f'{"Id":<5}{"Nome":^7} {"Média":>16}')
for i ,a in enumerate(lista_alunos):
    print(f'{i:<5} {a[0]:^5} {a[3]:>15.2f}')
print('-'*20)

while True:
    nota_individual = int(input('Digite o Id do aluno para ver a nota: [999 para PARAR]'))
    if nota_individual == 999:
        break
    print(f'A notas do Aluno: {lista_alunos[nota_individual][1]}, {lista_alunos[nota_individual][2]}')