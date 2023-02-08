#Crie um programa que leia dois valores e mostre um menu na tela:

#[ 1 ] somar

#[ 2 ] multiplicar

#[ 3 ] maior

#[ 4 ] novos números

#[ 5 ] sair do programa

#Seu programa deverá realizar a operação solicitada em cada caso.
while True:
    num1 = float(input('Numero1: '))
    num2 = float(input('Numero2: '))
    print('_'*30)
    print('CALCULADORA'.center(30))
    print('_'*30)
    menu = print('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos numeros
[5] Sair do Programa''')
    print('_'*30)
    escolha = int(input('Opção: '))
    print('_'*30)
    if escolha == 1:
        print(f'A soma dos valores é de: {num1 + num2}')
    elif escolha == 2:
        print(f' A Multiplicação dos valores é de: {num1 * num2}')
    elif escolha == 3:
        if num1 > num2:
            print(f' O mair número é: {num1}')
        else:
            print(f' O mair número é: {num2}')
    elif escolha == 4:
        num1 = float(input('Numero1: '))
        num2 = float(input('Numero2: '))
    elif escolha == 5:
        break