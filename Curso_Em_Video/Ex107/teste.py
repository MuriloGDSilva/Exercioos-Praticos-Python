from Ex107 import moeda
usuario = float(input('Insira um valor R$: '))
print(f' R${usuario} com 10% de aumento: {moeda.aumentar(usuario)}')
print(f' O dobro de R${usuario} é : {moeda.dobro(usuario)}')
print(f' Metade de R${usuario} é : {moeda.metade(usuario)}')
