# Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

def escreva(frase):
    print('-'* len(frase))
    print(frase)
    print('-'* len(frase))
escreva(input('Digite uma frase ou palavra: '))