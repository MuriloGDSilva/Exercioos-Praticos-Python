# Crie um programa que leia o nome de uma cidade e diga se ela começa com a palavra "Santo".
while True:
    cidade = str(input('Digite o nome completo da sua cidade: ')).title().strip()
    if cidade.isnumeric():
        print('Digite uma Cidade válida')
        pass
    else:
        if cidade[0] =='Santo':
            print('Sua Cidade começa com a palvara "Santo"')
            break
        else:
            print('Sua cidade não começa com a palavra "Santo"')
            break