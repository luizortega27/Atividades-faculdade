materias = ["Fundamentos de Banco de Dados", "Lógica de Programação", "Linguagem de Programação", "Matemática", "Internet of Things", "Comunicação e Expressão"]
posicao = 0
media_materias = [0] * 6

print("ATENÇÃO:\nÉ necessário a nota de no mínimo 4 Ac's para compor a média.\nCaso não tenha feito a última Ac, coloque a nota da mesma como 0.\n")

while posicao < len(media_materias):
    print("Insira a seguir as notas das Ac's de {}".format(materias[posicao]))

    ac_1 = float(input('Nota da 1º AC: ').replace(',', '.'))
    ac_2 = float(input('Nota da 2º AC: ').replace(',', '.'))
    ac_3 = float(input('Nota da 3º AC: ').replace(',', '.'))
    ac_4 = float(input('Nota da 4º AC: ').replace(',', '.'))
    ac_5 = float(input('Nota da 5º AC: ').replace(',', '.'))

    lista_notas = [ac_1, ac_2, ac_3, ac_4, ac_5]
    lista_notas.sort()
    del lista_notas[0]

    soma = sum(lista_notas)

    media_acs = round(soma/4, 2)
    nota_prova_final = (6 - (media_acs*0.5)) * 2
    media_maxima = (media_acs * 0.5) + 5

    print('=' * 17)
    print(' ')

    media_materias[posicao] = media_acs
    posicao += 1

posicao = 0
while posicao < len(media_materias):
    print("Média das Ac's em {}: {}".format(materias[posicao], media_materias[posicao]))
    print('Você presisa tirar no mínimo {:.2f} para passar com média 6.00.'.format(nota_prova_final))
    print('A média máxima possivel será {:.2f} caso tire 10.00 na prova final.'.format(media_maxima))
    print(' ')
    print('=' * 17)
    posicao += 1