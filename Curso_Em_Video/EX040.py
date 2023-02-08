#Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final,
# de acordo com a média atingida:

#– Média abaixo de 5.0: REPROVADO

#– Média entre 5.0 e 6.9: RECUPERAÇÃO

#– Média 7.0 ou superior: APROVADO

def media(nota):
    media = nota/2
    return media

notas = 0
for nota in range(0,2):
    aluno = int(input(f'{nota}° Nota: '))
    notas += aluno

if media(notas) <= 5:
    print(f'Aluno REPROVADO')
elif media(notas) > 5 and media(notas) <= 6.9:
    print(f'Aluno De RECUPERAÇÃO')
else:
    print(f'Aluno APROVADO')