#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Digite sua frase: ')).strip().upper()
f_separada = frase.split()
f_junta = ''.join(f_separada)
f_inversa = ''
for palavra in range(len(f_junta) - 1,-1,-1):
    f_inversa += f_junta[palavra]
if f_junta == f_inversa:
    print('A frase digitada é um palindromo')
else:
    print('A frase digitada não é um palindromo')