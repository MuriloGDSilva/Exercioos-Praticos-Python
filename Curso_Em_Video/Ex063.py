#Escreva um programa que leia um número N inteiro qualquer e
# mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:

#0 – 1 – 1 – 2 – 3 – 5 – 8

num = int(input('Digite um número para ver sua sequencia de fibonacci: '))
n1 = 0
n2 = 1
print(f'{n1} => {n2}',end=' => ')
for fibo in range(0,num):
     num = n1 + n2
     n1 = n2
     n2 = num
     print(num,end=' => ')
print('fIm'.upper())
