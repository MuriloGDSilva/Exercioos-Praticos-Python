#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
'''
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
'''

numeros = (int(input('Digite um Número: ')),int(input('Digiteum Número: ')),
           int(input('Digiteum Número: ')),int(input('Digiteum Número: ')))
print(f'Foram digitados um total de {numeros.count(9)} Noves.')
print(f'O valor 3° foi digitado na posição: {numeros.index(3) + 1}')
for n in numeros:
    if n % 2 == 0:
        print(f'Os números pares digitados foram: {n}')