#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(idade):
    from datetime import date
    idade = date.today().year - idade
    if idade >= 18:
        return f'Com {idade} Anos O Voto é Obrigatorio!'
    elif idade >= 16 and idade <= 18 or idade > 65:
        return f'Com {idade} Anos O Voto é Opcional'
    else:
        return f'Com {idade} Anos :Voto Negado!!'


nascimento = int(input('Digite seu Ano de Nascimento: '))
print('=' * 30)
print(voto(nascimento))