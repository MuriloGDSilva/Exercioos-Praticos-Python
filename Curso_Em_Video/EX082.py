#Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas
# os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

lista_numeros = []
while True:
    lista_numeros.append(int(input('Digite um número: ')))
    escolha = int(input(f'Deseja continuar: [1]Sim / [2] Não:  '))
    if escolha == 2:
        break
print(lista_numeros)
list_pares = []
lista_inpares = []
for numero in lista_numeros:
    if numero % 2 == 0:
        list_pares.append(numero)
    else:
        lista_inpares.append(numero)
print(list_pares)
print(lista_inpares)

