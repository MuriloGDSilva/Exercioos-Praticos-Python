#Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.
print('Gerador de tabuada'.center(40))
usuario = int(input('Insira um número ver sua tabuada: '))
fim = int(input('Até que número deseja que seja calculado ?: '))
for c in range(1,fim+1):
    print(f'{c} X {usuario}= {c*usuario}')