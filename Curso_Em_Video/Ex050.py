#Desenvolva um programa que leia seis números inteiros e
# mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

pares = 0
for num in range(1,7):
    usuario = int(input('Digite um número: '))
    if usuario % 2 == 0:
        pares += usuario
print(f'Soma de todos os numeros pares é de: {pares}')

    