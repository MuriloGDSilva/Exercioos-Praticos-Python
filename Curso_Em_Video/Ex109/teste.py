from Ex109 import moeda
usuario = float(input('Insira um valor R$: '))
print(f' {moeda.moeda(usuario)} com 10% de aumento: {moeda.aumentar(usuario,True)}')
print(f' O dobro de {moeda.moeda(usuario)} é : {moeda.dobro(usuario,True)}')
print(f' Metade de {moeda.moeda(usuario)} é : {moeda.metade(usuario,True)}')
