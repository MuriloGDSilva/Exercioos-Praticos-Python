#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

media = 0
maior_idade_homem = 0
nome_homem_velho = ''
contador_mulheres = 0


for pessoa in range(1,5):
    nome = str(input(f'Qual o nome da {pessoa}° pessoa: '))
    idade = int(input(f'Digite a idade da {pessoa}° pessoa: '))
    sexo = str(input(f'Digite o sexo da {pessoa}° pessoa [M/F]: ')).upper().strip()
    media += idade
    if pessoa == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_homem_velho = nome
    else:
        if sexo in 'Mm' and idade > maior_idade_homem:
            maior_idade_homem = idade
            nome_homem_velho = nome
    if sexo in 'Ff' and idade < 20:
        contador_mulheres += 1
print('Análisando dados......')
print(f'''A média de idade do grupo é de : {media / 4}
O nome do homem mais velho é {nome_homem_velho} com {maior_idade_homem} Anos.
O total de mulheres com menos de 20 é de {contador_mulheres}.
''')
