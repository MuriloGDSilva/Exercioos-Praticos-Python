#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e
#mostre sua categoria, de acordo com a idade:

#– Até 9 anos: MIRIM
#– Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER
from datetime import datetime

def idade_atual (nascimento):
    ano_atual = datetime.today().year
    idade = ano_atual - nascimento
    return idade


def categoria(idade):

    if idade <= 9:
        return f'O atleta tem {idade} Anos - Categoria MIRIM'
    elif idade > 9 and idade <= 14:
        return f'O atleta tem {idade} Anos - Categoria INFANTIL'
    elif idade > 14 and idade <= 19:
        return f'O atleta tem {idade} Anos - Categoria JÚNIOR'
    elif idade > 19 and idade <= 25:
        return f'O atleta tem {idade} Anos - Categoria SÊNIOR'
    else:
        return f'O atleta tem {idade} Anos - Categoria Master'

usuario = idade_atual(int(input('Insira o ano de nascimento do Atleta: ')))
print(categoria(usuario))
