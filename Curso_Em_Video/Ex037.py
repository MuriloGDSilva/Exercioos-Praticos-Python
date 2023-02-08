#Escreva um programa em Python que leia um número inteiro qualquer e
# peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

numero = int(input('Digite um número inteiro: '))
print('''Escolha uma opção para converter
[1] Para converter para BINÁRIO
[2] Para Converter para OCTAL
[3] Para Converter para HEXADECIMAL''')
escolha =  int(input('Digite sua Opção: '))

if escolha == 1:
    print(f'{numero} convertido pra BINÁRIO: {bin(numero)[2:]}')
elif escolha == 2:
    print(f'{numero} convertido em OCTAL: {oct(numero)[2:]}')
elif escolha == 3:
    print(f'{numero} convertido para HEXADECIMAL: {hex(numero)[2:]}')
