#Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular (largura e comprimento)
# e mostre a área do terreno.

def area(b,a):
    area = b*a
    return area
print('CALCULE A ÁREA DO SEU TERRENO'.center(40))
base = float(input('Base m²: '))
altura = float(input('Altura m²: '))
print(f'Seu terreno tem uma area total de: {area(base,altura)} m²')