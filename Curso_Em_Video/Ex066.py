# Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 0,
# que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

soma = 0
contador = 0
while True:
    numero = int(input('Digite um número: [0 para parar]: '))
    if numero == 0:
        break
    soma += numero
    contador += 1
print(f'Foram digitados {contador} Números, E soma entre eles é de: {soma}')