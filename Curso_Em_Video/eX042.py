#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

#– EQUILÁTERO: todos os lados iguais

#– ISÓSCELES: dois lados iguais, um diferente

#– ESCALENO: todos os lados diferentes


lado_a = float(input('Insira o comprimento do 1° lado: '))
lado_b = float(input('Insira o comprimeto do 3° lado: '))
lado_c = float(input('Insira o comprimento do 3° lado: '))
if lado_a == lado_b and lado_b == lado_c:
    print(f'De acordo co as medidas passadas elas fomam um triangluo:\n'
          f'< EQUILÁTERO >')
elif lado_a != lado_b and lado_b != lado_c:
    print(f'De acordo co as medidas passadas elas fomam um triangluo:\n'
          f'< ESCALENO >')
else:
    print(f'De acordo co as medidas passadas elas fomam um triangluo:\n'
          f'< ISÓSCELES >')