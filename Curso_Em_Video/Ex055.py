# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

lista_pesos = list()
while True:
    lista_pesos.append(float(input('Digite o peso: ')))
    escolha = input('Continuar ? [S/N]: ').strip().upper()[0]
    if escolha in 'N':
        break
print(f'Maior peso: {max(lista_pesos)}\nMenor peso: {min(lista_pesos)}')