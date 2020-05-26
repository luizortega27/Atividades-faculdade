n= int(input())
if n < 1 or n > 5:
    print("Numero de notas invalido.")
    
else:
    notas = 5 * [1]
    pos = 0

    while pos < n:
        notas[pos] = float(input())
        pos= pos+1
    
    var1 = 0
    pos = 0
    indice = 1

    while pos < n:
        print("Nota {}: {}".format(indice,notas[pos]))
        var1 = var1 + notas[pos]
        pos = pos + 1
        indice = indice + 1
    var2 = (var1 /n)
    print("Media:"" {:.2f}".format(var2)) 