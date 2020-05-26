valor = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

for nota in notas:
    qtd_nota = int(valor / nota)
    print('{} nota(s) de R$ {:.2f}'.format(qtd_nota, nota))
    valor -= qtd_nota * nota

for moedas in moedas:
    qtd_moedas = int(round(valor,2) / moedas)
    print('{} moedas(s) de R$ {:.2f}'.format(qtd_moedas, moedas))
    valor -= qtd_moedas * moedas

