# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.
from time import sleep
velocidade = float(input("Insira sua velocidade:  "))
print('Analisando velocidade.....')
sleep(3)
if velocidade > 80:
    print(f'VocÊ será multado no valor de: {(velocidade - 80) * 7}')
