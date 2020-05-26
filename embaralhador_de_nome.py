import random

aluno = int(input('Quantidade de alunos: '))
list_aluno = []

print('='*25)

cont = 1
while cont <= aluno:
    name_aluno = input('Nome do {}º aluno: '.format(cont))
    list_aluno.append(name_aluno)
    cont+=1

print('='*25)

print('Nomes inseridos:')
cont2 = 1
for name in list_aluno:
    print('Aluno {} - {}'.format(cont2,name))
    cont2+=1

print('='*25)

list_random = []
while len(list_random) < len(list_aluno):
    num_random = int(random.random() * (int('1'+(len(str(aluno))*'0'))))
    if num_random < len(list_aluno) and num_random not in list_random:
        list_random.append(num_random)

print('Nomes embaralhados:')
cont3 = 1
for i in list_random:
    print('Aluno {}- {}'.format(cont3,list_aluno[i]))
    cont3+=1

print('='*25)