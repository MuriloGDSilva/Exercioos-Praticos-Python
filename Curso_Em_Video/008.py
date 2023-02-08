# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

print('----Conversor de médida----'.upper())
medida = float(input('Digite a Médida que deseja converter: '))
print(f'A médida de {medida} convertida em:\nCemtimetros: {medida * 100}\nMilimetros: {medida * 1000}')
print('=-=' * 20)
