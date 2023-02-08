#Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.

tot_p18 = 0
tot_h = 0
tot_m20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [Masculino / Feminino]: ')).upper()[0]
    if idade >= 18:
        tot_p18 += 1
        if sexo in 'M':
            tot_h += 1
    elif idade < 20 and sexo in 'F':
        tot_m20 += 1

    escolha = input('Continuar? ').upper().strip()[0]
    if escolha in 'N':
        break
print(f'Total de pessoas com 18+: {tot_p18}\nTotal de Homens: {tot_h}\nTotal de Mulheres com -20: {tot_m20}')