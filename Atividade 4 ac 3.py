n=int(input())

denominador= 1
var= 0
contador=1

while contador <= n:

    if (denominador%2) == 0:
        var += 1/denominador
        denominador += 1
        contador += 1

    else:
        var -= 1/denominador
        denominador += 1
        contador += 1

print("{:.6f}".format(var))