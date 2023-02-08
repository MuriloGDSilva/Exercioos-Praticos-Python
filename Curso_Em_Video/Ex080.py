#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.

numeros = list()
contador = 0
while True:
    usuario_num = int(input('Insira um número: '))
    continuar = input('Adicionar mais números ?: [Sim/Não]: ').strip().upper()[0]
    if continuar in 'N':
        break
    if contador == 0 or usuario_num > numeros[-1]:
        numeros.append(usuario_num)
        contador += 1
    else:
        if usuario_num <= numeros[0]:
            numeros.insert(0,usuario_num)
        elif usuario_num <= numeros[1]:
            numeros.insert(2,usuario_num)




print(numeros)