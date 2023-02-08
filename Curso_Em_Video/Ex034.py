#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. -Para salários superiores a
# R$1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Insira o valor do seu sálario: '))
aumento_15 = salario + (salario * 15/100)
aumento_10 = salario + (salario * 10/100)
if salario >= 1.250:
    print(f'Seu sálario tera´um aumento de 10%\nSalario antigo: {salario}\nSálario novo: {aumento_10}')
else:
    print(f'Seu sálario terá um aumento de 15%\nSálario antigo; {salario}\nSálario novo: {aumento_15}')
print('¨' * 25)