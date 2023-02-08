#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date

pessoa = dict()
pessoa['nome'] = input('Nome: ').strip()
ano_nascimento = int(input('Ano de nascimento: '))
idade = date.today().year - ano_nascimento
pessoa['idade'] = idade
pessoa['CTPS'] = int(input('Número da sua carteira de trabalho: '))
if pessoa['CTPS'] != 0:
    pessoa['ano de contaratação'] = int(input('Ano de contratação: '))
    pessoa['Sálario'] = float(input('Sálario atual: '))
    pessoa['Aposentadoria'] = (pessoa['idade'] + (pessoa['ano de contaratação'] + 35) - date.today().year)
print('_-'*30)
for k , v in pessoa.items():
    print(f'{k}: {v}')