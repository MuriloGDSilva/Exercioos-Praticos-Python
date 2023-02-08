#Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.

def ajuda(msg):
    print('=='*50)
    print(cores['amarelo'])
    help(msg)
    print(cores['padrao'])
    print('=='*50)


def titulo(texto,cor='padrao'):
    tam = len(texto) + 8
    print(cores[cor], end='')
    print(f'    {texto}    ')
    print(cores["padrao"], end='')

cores =  {
    'padrao': '\033[m',
    'vermelho': '\033[0;30;41m',
    'verde': '\033[0;30;42m',
    'amarelo': '\033[0;30;43m',
    'azul': '\033[0;30;44m',
    'roxo': '\033[0;30;45m',
    'branco': '\033[0;30m'
}
titulo('PyHelp','verde')
while True:
    usuario = input('Digite a Função ou Biblioteca que precisa de ajuda: (FIM, para parar): ')
    if usuario.upper() in 'FIM':
        break
    else:
        ajuda(usuario)
print(cores['vermelho'])
print('<PROGRAMA ENCERRADO>')
print(cores['padrao'])
