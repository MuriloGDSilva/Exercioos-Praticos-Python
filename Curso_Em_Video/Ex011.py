#Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessaria
#para pintala, sabendo que cada litro de tinta pinta uma area de 2m².
lagura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
resultado = (lagura * altura) / 2
print(f'Você precisará de {resultado} litros de tinta.\nNo caso de duas demãos você precisará de: {resultado * 2} litros.')
