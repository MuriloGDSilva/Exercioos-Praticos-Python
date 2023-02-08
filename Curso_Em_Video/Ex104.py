#Crie um programa que tenha a função leiaInt(),
# que vai funcionar de forma semelhante ‘a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt(‘Digite um n: ‘)


def leiaint(num=0):
    while True:
        num = str(input('Insira um numero: '))
        if num.isnumeric():
            return (f'Voce Digitou o número {num}.')
        else:
            print(f'\033[0;31mERRO!!\033[m,\033[4;32mDigite apenas números inteiros\033[m')

print(leiaint())