# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
contador = 0
while True:
    sexo = input('Digite o sexo dá pessoa [M/F]: ')
    while sexo not in 'MF':
        sexo = input('Digite o sexo dá pessoa [M/F]: ').upper().strip()[0]
        contador += 1
        if contador <= 3:
         print('Digite apenas M OU F')
        elif contador > 3:
            print('Você é uma anta por acaso. APENAS [M OU F]')
    if sexo in 'MF':
        break
print('Obrigado ')