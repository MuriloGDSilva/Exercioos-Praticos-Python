#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
lista_numerica = []
escolha = 0
while escolha != 2:
    numeros =(int(input('Digite um valor: ')))
    if numeros in lista_numerica:
        print(f'Número duplicado')
    else:
        lista_numerica.append(numeros)
    escolha = int(input('Deseja comtinuar ? [1] Sim / [2] Não: '))
    print('='*30)
lista_numerica.sort()
print(f'Toal de números digitados: {len(lista_numerica)}')
print(f'Numeros digitados em ordem crescente: {lista_numerica}')