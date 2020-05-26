
lista = input().split()

cont = 0

while cont < len(lista):
    lista[cont] = int(lista[cont])
    cont = cont + 1

enter = input().split()

if len(enter) == 2:
    var = int(enter[1])

while enter[0] != "final":
    if enter[0] == "inserir":
        lista.append(var)
    if enter[0] == "remover":
        lista.remove(var)
    if enter[0] == "parcial":
        var = sorted(lista)
        print(*var, sep = " ")

    enter = input().split()
    if len(enter) == 2:
        var = int(enter[1])

var = sorted(lista)
print(*var, sep = " ")







