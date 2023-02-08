#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import datetime
valido = False
usuario = 0
while valido == False:
    usuario = int(input('Insira a data de nascimento: '))
    if len(str(usuario)) > 4:
        print('Insira um data válida.')
    else:
        valido = True

idade = datetime.today().year - int(usuario)
if idade < 18:
    print(f'Voce atualmete tem: {idade} Anos, Voce se alistara daqui a {18 - idade} Anos.')
elif idade >= 18 and idade <= 60:
    print(f'Voce tem {idade} Anos, Voce precisa se alistar imediatamente!.')
elif idade > 60:
    print(f'Pessoas com mais de 60 Anos não é obrigatorio o alistamento.')