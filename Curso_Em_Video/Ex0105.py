#Faça um programa que tenha uma função notas()
# que pode receber várias notas de alunos e
# vai retornar um dicionário com as seguintes informações:
#– Quantidade de notas
#– A maior nota
#– A menor nota
# – A média da turma
#– A situação (opcional)

def notas(*n,sit=False):
    alunos= dict()
    alunos['Total_De_notas:'] = len(n)
    alunos['Maior_Nota:'] = max(n)
    alunos['Menor_Nota:'] = min(n)
    alunos['Média_Turma:'] = sum(n)/len(n)
    if sit == True:
        if alunos['Média_Turma:'] < 5:
            alunos['Situação:'] = 'Ruim'
        elif  alunos['Média_Turma:'] >= 5 and alunos['Média_Turma:'] <= 7:
            alunos['Situação:'] = 'Razoavel'
        elif alunos['Média_Turma:'] > 7:
            alunos['Situação:'] = 'Boa'
    return alunos
print(notas(4,2,sit=True))