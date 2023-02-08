#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

def analise_cred(casa_v,salario_a,tot_anos):
    valor_parcela = casa_v / (tot_anos * 12)
    if valor_parcela > (30 * salario_a)/100:
        return '\033[31mEmprestimo Negado!!\033[0m' \
               'O valor da parcela excede 30% do seu sálario'
    else:
        return f'\033[0;32mEmprestimo Aprovado!!\033[0m' \
               f'Valor da parcela: {valor_parcela:.2f}'

print(f'\033[33;40m{"Agencia de Empretimo Imobiliario":/^50}\033[0m')
valor_casa = float(input('Insira o valor da casa: '))
salario_usuario = float(input('Seu sálario Atual: '))
parcela_anos = int(input('Total de anos que deseja pagar: '))
print('_-'*30)
print(analise_cred(valor_casa,salario_usuario,parcela_anos))