from Ex108 import moeda
usuario = float(input('Insira um valor R$: '))
print(f' {moeda.moeda(usuario)} com 10% de aumento: {moeda.moeda(moeda.aumentar(usuario))}')
print(f' O dobro de {moeda.moeda(usuario)} é : {moeda.moeda(moeda.dobro(usuario))}')
print(f' Metade de {moeda.moeda(usuario)} é : {moeda.moeda(moeda.metade(usuario))}')
