# Faça um programa que leia uma frase pelo teclado e mostra:
# Quantas vezes aparece a letra 'A'.
# Em que posiçao ela aparece a primeira vez.
# Em que posiçao ela aparece a ultima vez.

def analisador_frase(msg):
    '''
    . Função pra analisar uma frase
    :param msg: Recebe uma frase
    :return: NONE
    '''
    tot_A = msg.count('a')
    print(f'Foi analisado um total de {tot_A} A(s)')
    primeira_Pos = msg.find('a')
    print(f'O primeiro "A" aparece na posição: {primeira_Pos}')
    ultima_pos = msg.rfind('a')
    print(f'O ultimo "A" aparece na posição: {ultima_pos}')


frase = input('Insira uma frase para analise: ').strip().lower()
print('\033[0;33;34m-\033[0m'*60)
analisador_frase(frase)