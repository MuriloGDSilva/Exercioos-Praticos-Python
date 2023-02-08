# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.


contador = 0
num = 0
while True:
    try:
        usuario = int(input('Digite um número: '))
    except(TypeError,ValueError):
        print('Por Favor digite apenas números inteiros')
        continue
    else:
        num += usuario
        contador +=1

    escolha = str(input('Cotinuar [Sim/Não]: ')).upper().strip()[0]
    if escolha in 'N':
        break
    elif escolha in 'S':
        continue
    else:
        print('ERRO! Não existe essa opção!!')
        escolha = str(input('Cotinuar [Sim/Não]: ')).upper().strip()[0]
        if escolha in 'N':
            break


print(f' A Soma dos números fornecidos é:{num} e sua média é de: {num/contador}')