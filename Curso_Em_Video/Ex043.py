#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
# e mostre seu status, de acordo com a tabela abaixo:

#IMC abaixo de 18,5: Abaixo do Peso
 #Entre 18,5 e 25: Peso Ideal
 #25 até 30: Sobrepeso
 #30 até 40: Obesidade
#Acima de 40: Obesidade Mórbida

def imc(p,a):
    Imc = p / (a**2)
    print(f'Seu Indice de Massa Corporal: {Imc:.2f}')
    if Imc > 40:
        print(f'Essa pessoa está com Obesidade Mórbida, Por favor Procre um Médico urgente!!!')
    elif Imc >= 30 and Imc <= 40:
        print(f'Essa pessoa está com Obesidade , Procure um Médico!!!')
    elif Imc >= 25 and Imc <= 30:
        print(f'Essa pessoa está com Sobre peso, Recomendos uma dieta antes que o quadro se agrave!!!')
    elif Imc >= 18.5 and Imc <= 25:
        print(f'Essa pessoa está com Peso Ideal: Parabéns!!')
    elif Imc < 18.5:
        print(f'Essa pessoa está abaixo do peso , Por favor Procure um Médico !!!')

peso = float(input('Peso:  '))
altura = float(input('Altura: '))
imc(peso,altura)

