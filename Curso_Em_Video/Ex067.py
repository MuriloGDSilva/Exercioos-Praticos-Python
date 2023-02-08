#Faça um programa que mostre a tabuada de vários números, um de cada vez,
# para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.


def tabuada(num=0):
        for x in range(1,10):
            print(f'{x} X {num} = { x * num}')
        print('_'*30)


while True:
    usuario = int(input('Insira o número: '))
    if usuario < 0:
        break
    tabuada(usuario)
print('_'*20)
print('Programa encerrado'.upper())