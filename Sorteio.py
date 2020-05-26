import random

alunos = int(input())
quant = int(input())

lista=[]
cont=0
rodadas = 0

while alunos < 1 or alunos > 20:
    alunos = int(input())

while  alunos > cont:
    cont= cont + 1
    name_aluno = input()
    lista.append(name_aluno)

n = random.randint(1,alunos)
cont=0
resulta = ""


while not n == cont:
    resulta = lista[n]
    cont= cont +1
    rodadas = rodadas +1

print(resulta)