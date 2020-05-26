x = int(input())
n = int(input())
contador = 1
var = 0
valor = 0
while valor < n:
   contador = contador + 1
   valor = x * contador
   var = var + 1

   
print('O numero {} tem {} multiplos menores que {}.'.format(x,var,n))
