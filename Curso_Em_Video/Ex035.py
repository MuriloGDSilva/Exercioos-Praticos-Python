#Desenvolva um programa que leia o comprimento de três retas e
# diga ao usuário se elas podem ou não formar um triângulo.

lado_a = float(input('Insira o comprimento do 1° lado: '))
lado_b = float(input('Insira o comprimeto do 3° lado: '))
lado_c = float(input('Insira o comprimento do 3° lado: '))
if lado_a + lado_b > lado_c:

    print('As tres medidas formam um triangulo')
else:

    print('AS tres retas não formam um triangulo')