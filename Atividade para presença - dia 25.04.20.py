
    ##Retorna a soma de a e b (a + b)
def soma (a, b) :
    soma = (a + b)
    print('A soma é:', soma)
    pass

##    Retorna a subtração de a por b (a - b)
def subtrai (a, b) :
    subtrai = (a - b)
    print('A subtração:', subtrai)
    pass

##    Retorna o produto de a e b (a * b)
def multiplica (a, b) :
    multiplica = (a * b)
    print('A multiplicação é:', multiplica)
    pass

##    Retorna a divisão de a por b (a / b)
def divide (a, b) :
    divide = (a / b)
    print('A multiplicação é:', divide)
    pass

## Exibe um menu para o usuário listando as opções 1 para somar, 2 para subtrair, etc e 0 para encerrar.

def exibe_menu():
    print('''Digite:
1 Para SOMAR
2 Para SUBTRAIR
3 Para MULTIPLICAR
 4 Para DIVIDIR
0 Para ENCERRAR''')
    
    nr = int(input("Insira \n"))
    while nr != 0:
        if nr == 1:
           print('SOMA')
           a, b = numeros()
           soma = (a, b)
            
        if nr == 2:
           print('SUBTRAÇÃO')
           a, b = numeros()
           subtrai = (a, b)

        if nr == 3:
           print('MULTIPLICAÇÃO')
           a, b = numeros()
           multiplica = (a, b)

        if nr == 4:
           print('DIVISÃO')
           a, b = numeros()
           divide = (a, b)
        
        print('''Digite:
1 Para SOMAR
2 Para SUBTRAIR
3 Para MULTIPLICAR
4 Para DIVIDIR
0 Para ENCERRAR''')
    
        nr = int(input("Insira \n"))

    if nr == 0:
        print('o número informado não é válido!')
    pass

def numeros():
    a = float(input('Primeiro valor \n' ))
    b = float(input('Segundo valor \n')) 
    return (a, b)
    pass

def calculadora():
    exibe_menu()
    pass

calculadora() 