msg = str(input())
cod = str(input())

def contem(msg, cod):
    var = 0
    for item in msg:
        if item == cod:
            var += 1
    if var > 0:
        print('O caractere buscado ocorre',var,'vezes na sequencia.')
    else:
        print('Caractere nao encontrado.')       
    return

contem(msg,cod)