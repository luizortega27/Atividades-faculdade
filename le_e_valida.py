


def le_e_valida(a, b, msg) :
    if (dia >=1 and dia <=28) and (mes >=1 and mes <=12) and (desconto_percentual >= 0 and desconto_percentual <= 100):
    pass        

le_e_valida(a, b, msg)

nome = 0
dia = 0
mes = 0
total = 0
desconto_percentual = 0


def exibe_total(nome, dia, mes, total, desconto_percentual) :

   
    print('\n {}/{} - {} \n Valor total R$: {} \n Valor com desconto R$: {}'.format(dia,mes,nome,total,(total-(total*desconto_percentual/100))))
    pass



qtd_pessoas = int(input('Digite o número de clientes:\n'))

def registra_atendimentos(qtd_pessoas):
    cont = 1

    while cont <= qtd_pessoas:

        nome = str(input('Digite o nome:\n'))
        dia = int(input('Digite o dia:\n'))
        mes = int(input('Digite o mês:\n'))
        total = int(input('Digite o total:\n'))
        desconto_percentual = float(input('Digite o percentual do desconto de 0 a 100%:\n'))
        exibe_total(nome, dia, mes, total, desconto_percentual)
    cont =+ 1
    
registra_atendimentos(qtd_pessoas)

