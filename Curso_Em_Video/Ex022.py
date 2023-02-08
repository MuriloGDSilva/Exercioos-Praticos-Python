# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maisuculas
# O nome com todas minusculas
# Quantas letras ao todo (Sem considerar espaços)
# Quantas letras tem o primeiro nome


nome = input('Nome: ').strip()
print('_'*30)
print(f'Nome em letras maisuculas: {nome.upper()}')
print('_'*30)
print(f'Nome em letras minusculas: {nome.lower()}')
print('_'*30)
print(f'Total de letras no seu nome: {len(nome) - nome.count(" ")}')
print('_'*30)
print(f'Totol de letras no primeiro nome: {len(nome.split()[0])}')