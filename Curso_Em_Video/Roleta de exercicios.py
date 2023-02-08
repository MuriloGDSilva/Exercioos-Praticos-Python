from random import randint
from time import sleep

print(f'{"Gerador de exercios":#^30}')
menu = '''[1] Ver Exercios já Feitos
[2] Gerar Novo Exercicio'''
print('_' * 30)
print(menu)
print('_' * 30)
escolha_usuario = int(input('Digite sua opção: '))
print('_' * 30)
sleep(1)
if escolha_usuario == 1:
    arquivo = open('Exercicios_feitos', 'r')
    print(arquivo.read() + '\n')
elif escolha_usuario == 2:
    while True:
        print(f'Gerando Exercicios....'.title())
        sleep(1)
        exercio = str(randint(10, 106))
        arquivo = open('Exercicios_feitos', 'r')
        if exercio in arquivo.read():
            print(f'Exercicio {exercio} já feito')
            arquivo.close()
        else:
            print(f'Exercico Selecionado: {exercio}')
            arquivo = open('Exercicios_feitos', 'at')
            arquivo.write(f'{exercio}\n')
            break
print('_' * 30)
