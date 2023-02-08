#  Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
#  mostrando os 10 primeiros termos da progressão usando a estrutura while.

termo = int(input('Digite o 1° Termo: '))
razao = int(input('Digite a razão: '))

decimo = 10
contador = 0

while decimo >= contador :
    termo += razao
    contador += 1
    print(termo, end='-')
print('FIM')