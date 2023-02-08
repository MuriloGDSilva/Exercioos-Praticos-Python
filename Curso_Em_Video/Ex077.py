#Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('Fotocopiadora', 'Medida', 'Engano','Grao','pinturas')
vogais = 'aeiou'
for p in palavras:
    print(f'\n{p}',end='->')
    for v in p.lower():
        if v in vogais:
            print(f'{v}',end=', ')

