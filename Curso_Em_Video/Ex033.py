# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
m = mn = 0
c = 1
escolha = ''
while escolha != 'N':
    try:
     usuario = float(input(f'Insira o {c}° Número:  '))
    except(TypeError,ValueError):
        print('Erro!')
        continue
    if c == 1:
        m = usuario
        mn = usuario
    else:
        if usuario > m:
            m = usuario
        elif usuario < mn:
            mn = usuario
    c+=1
    while True:
        try:
            escolha = str(input('Quer continuar ?')).upper()[0]
        except(TypeError,ValueError):
            print('Não existe essa opção!!')
            continue
        if escolha.isnumeric():
            print('ERRO! Não existe essa opção')
        else:
            break
    if escolha in 'N':
        break
    elif escolha in 'S':
        continue

print(f'O maior número inseriodo foi: {m}\nO menor número inserido foi: {mn}')
