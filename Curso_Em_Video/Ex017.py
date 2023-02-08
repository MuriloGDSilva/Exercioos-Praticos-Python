# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangula retalgulo,
#calcule e mostre o comprimento da hipotenusa.

from math import hypot

cateto_oposto = float(input('Insira a médida do cateto Oposto: '))
cateto_adjacente = float(input('Insira a médida do cateto Adjacente: '))
print('  calculando...'.upper())
print(f'O valor da Hypotenusa: {hypot(cateto_oposto, cateto_adjacente):.2f}<---')