#Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

tot_numeros = 0
soma = 0
while True:
    usuario = int(input('Digite um número:[999 Prar PARAR]:  '))
    if usuario == 999:
        break
    tot_numeros += 1
    soma += usuario
print(f'Total de números digitados: {tot_numeros}')
print(f'A soma de todos os números é de: {soma}')