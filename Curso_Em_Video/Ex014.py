#Escreva um programa que converta uma temperatura digitada em °C e converta para °F.

temperatura = float(input('Digite a temperatura: '))
print('-----Fazendo a conversão de C°para F° -----'.upper())
print(f'Sua temperatura convertida == F°{(temperatura * 9/5) + 32}')
print('-' * 45)