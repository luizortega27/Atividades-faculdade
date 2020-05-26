n = int(input())
while n < 1 or n > 9:
    print("Insira um número inicial entre 1 e 9")
    n = int(input())
n1 = int(input())

while n1 < 1 or n1 > 9:
    print("Insira um número final entre 1 e 9")
    n1 = int(input())
    
if ( n > n1):
    print("Nenhuma tabuada nesse intervalo")

cont = 0

while n <= n1:
    for cont in range(0,9):
        cont = cont + 1
        print('{} x {} = {}'.format(n,cont,(n*cont)))
    print()
    n = n+1  