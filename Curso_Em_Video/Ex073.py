# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
# do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#
# a) Os 5 primeiros times.
#
# b) Os últimos 4 colocados.
#
# c) Times em ordem alfabética.
#
# d) Em que posição está o time da Chapecoense.

taela_colocacao = ('Palmeiras','Internacional','Corinthians','Flamengo',
                   'Fluminense','Athletico-PR','Atlético-MG','América-MG',
                   'Botafogo','Fortaleza','Santos','São Paulo',
                   'Bragantino','Goiás','Coritiba','Ceará',
                   'Cuiabá','Atlético-GO','Avaí','Juventude')

print(f'Os cincos prieiros times da tabela: {taela_colocacao[:5]}')
print(f'Os ultimos 4 colocados da tabela : {taela_colocacao[-4:]}')
print(f'Os times em ordem alfabética: {sorted(taela_colocacao)}')
print(f'Em que posição está o time do Chapecoense: O time da Chapecoense não esta entre os vinte colocados')