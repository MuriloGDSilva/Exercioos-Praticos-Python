#Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0,0,0], [0,0,0], [0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite o numero para a posição {l,c}: '))
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end=' ')
    print()
pares = 0
for num in matriz:
    for d in num:
        if d%2 == 0:
            pares += d
print(f'A soma dos pares é de: {pares}')
terceira_coluna = 0
for l in range(0,3):
    terceira_coluna += matriz[l][2]
print(f'O soam dos valores da Terceira Coluna é de: {terceira_coluna}')
maior = 0
for l in range(0,3):
    if l == 0:
        maior= matriz[1][l]
    elif matriz[1][l] >= maior:
        maior=matriz[1][l]
print(f'O maior valor da senuda linha é: {maior}')