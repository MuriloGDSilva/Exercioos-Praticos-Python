def leiaint(msg):
    while True:
        try:
         num = int(input(msg))
         return num

        except(TypeError,ValueError):
            print('\033[31;1mERRO!\033[m\033[4;33m-> Digite somente números inteiros\033[m')
            continue
        except(KeyboardInterrupt):
            print('O usuario não quis continuar')
            break


def linha(tam=40):
    print('-'*tam)


def cabesalho(texto):
    linha()
    print(f'{texto:^40}')
    linha()


def opcoes(lista_opcoes):
    c = 1
    for opcao in lista_opcoes:
        print(f'\033[33m{c}\033[m->\033[34m{opcao}\033[m')
        c +=1
    linha()


def pessoas_cadastradas(valor=0):
    try:
        with open('curso_em_video.txt','r') as arquivo:
            for p in arquivo:
                print(p)
    except:
        print('Erro!!')

def cadastrar_pessoa(nome,idade):
    valor = input((msg))
    try:
        with open('curso_em_video.txt','a') as arquivo:
            arquivo.write(str(valor) +"\n")
    except:
        print('Erro!')
