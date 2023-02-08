#Crie um programa onde o usuário possa digitar sete valores numéricos e
# cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.

lista_numeros = [[], []]
for numeros in range (1,8):
    numero = int(input(f'Digite o {numeros}° valor: '))
    if numero % 2 == 0:
         lista_numeros[0].append(numero)
    else:
        lista_numeros[1].append(numero)
lista_numeros[0].sort()
lista_numeros[1].sort()
print(f'Lista de números pares: {lista_numeros[0]}\nLista de números ímpares: {lista_numeros[1]}')