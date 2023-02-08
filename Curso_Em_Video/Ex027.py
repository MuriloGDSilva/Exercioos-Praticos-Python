# Faça um programa que leia o nome completo de uma pessoa,Mostrando em seguida
# o primeiro e o ultimo nome separadamente.
    # Exemplo: nome: Murilo Gomes da Silva
                # primeiro nome: Murilo
                # Ultimo nome: Silva

nome = str(input("Digite seu nome completo: ")).strip().split()
print(f'Seu primeiro nome: {nome[0]}\nSeu último nome: {nome[-1]}')