#Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

termo = int(input('Termo: '))
razao = int(input('Razão: '))
termos = int(input('Quantidade de termos: '))
contador = 0
while True:
    contador = 0
    while contador < termos:
        termo+=razao
        print(f'{termo}',end='->')
        contador +=1
    termos = int(input('\ntermos a mais quer mostrar ?: '))
    if termos == 0:
        break