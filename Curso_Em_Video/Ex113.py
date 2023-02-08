#Reescreva a função leiaInt() que fizemos no desafio 104,
#incluindo agora a possibilidade da digitação de um número de tipo inválido.
#Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaint(msg):
    while True:
        try:
         num = int(input(msg))
         return num

        except(TypeError,KeyboardInterrupt,ValueError):
            print('\033[31;1mERRO!\033[m\033[4;33m-> Digite somente números inteiros\033[m')
            continue

def leiafloat(msg):
    while True:
        try:
            num = float(input(msg))
            return num
        except(TypeError,KeyboardInterrupt,ValueError):
            print('\033[31;1mERRO!\033[m\033[4;33m-> Digite somente números inteiros\033[m')
            continue

usuario = leiaint('Digite um número inteiro: ')
print(f'Voce digitou o número: {usuario}')
print('_'*30)
usuario_f = leiafloat('Digite um número real:')
print(f'O número real digitado foi: {usuario_f}')