# Crie um programa que leia o nome de uma pessoa e diga se ela  tem "silva" no nome.

nome = input('Digite seu nome: ').strip().title().split()
for p in nome:
    if p == 'Silva':
        print('Voce possui "Silva " em seu nome.')
        break
print('Voce não poussui "Silva" em seu nome.')