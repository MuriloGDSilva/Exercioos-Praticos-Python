# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,
# mostre os 10 primeiros termos dessa progressão.

termo = int(input('Digite o 1° termo: '))
razao = int(input('Digite a razão: '))
decimo = termo + razao * (10 - 1)
for contador in range(termo, decimo + 1, razao):
    print(contador)