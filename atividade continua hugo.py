def le_e_valida(a, b, msg):
    dia = 0
    mes = 0
    desconto_percentual = 0
    while dia < a or dia > b:
        print(msg, a, ' e ', b)
        dia = int(input())
    return dia
    while mes < a or mes > b:
        print(msg, a, ' e ', b)
        mes= int(input())
    return mes
    while desconto_percentual < a or desconto_percentual > b:
        print(msg, a, ' e ', b)
        desconto_percentual= float(input())
    return desconto_percentual    





def exibe_total(nome, dia, mes, total, desconto_percentual):

     print(dia,'/',mes, '-' ,nome)
     print('Valor total: ', total)
     print('Valor com desconto: {:.2f}'.format(total-((total*desconto_percentual)/100)))


def registra_atendimento(qtd_pessoas):

    cont = 1
    while cont <= qtd_pessoas:

        nome = str(input('Nome do cliente: '))
        dia = (le_e_valida(1, 28, 'Dia do mês deve estar entre '))
        mes = (le_e_valida(1, 12, 'O mês deve estar entre '))
        total = float(input('Valor total: '))
        desconto_percentual = le_e_valida(0, 100, 'O desconto deve ser entre ')

        exibe_total(nome, dia, mes, total, desconto_percentual)

        cont+=1


qtd_pessoas = int(input('Quantidade de pessoas: '))

registra_atendimento(qtd_pessoas)

