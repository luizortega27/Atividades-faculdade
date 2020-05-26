
N, K = input().split(" ")

K = int(K)
N = int(N)

lista=[]
cont=0

while  N > cont:
    cont= cont + 1
    name_aluno = input()
    lista.append(name_aluno)

lista.sort()

K = K-1

print(lista[K])