#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expressao = str(input('Digite sua expressão: '))
lista_simbol = []
for simbolo in expressao:
    if simbolo == '(':
        lista_simbol.append('(')
    elif simbolo == ')':
        if len(lista_simbol) > 0:
            lista_simbol.pop()
        else:
            lista_simbol.append(')')
if len(lista_simbol) == 0:
    print(f'Sua expressão é válida.')
else:
    print(f'Sua expressão não é válida.')

