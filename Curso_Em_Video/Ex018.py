# Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno,cosseno e tangente desse angulo.

from math import sin,cos,tan,radians

angulo = float(input('Digite o Ângulo: '))
angulo_2 = radians(angulo)
print(f'Seno: {sin(angulo_2):.2f}\nCossno: {cos(angulo_2):.2f}\nTangente: {tan(angulo_2):.2f}')
