valor = float(input())

valor = float(valor*100)

    
n100 =int(valor / 10000)
valor = valor % 10000
n50 = int(valor / 5000)
valor = valor % 5000
n20 = int(valor / 2000)
valor = valor % 2000
n10 = int(valor / 1000)
valor = valor % 1000
n5= int(valor / 500)
valor = valor % 500
n2 = int(valor / 200)
valor = valor  % 200


ms1 = int (valor/100)
valor = ( valor % 100)
m50 = int (valor/50)
valor = ( valor % 50)
m25 = int (valor / 25)
valor = (valor % 25)
m10 = int (valor / 10)
valor =  (valor %  10)
m5 = int (valor/5)
valor = ( valor %  5)
m01 = int  (valor/1)





if n100:
    print(n100,"nota(s) de R$ 100.00")
if n50:
    print(n50,"nota(s) de R$ 50.00")
if n20:
    print(n20,"nota(s) de R$ 20.00")
if n10:
    print(n10,"nota(s) de R$ 10.00")
if n5:
    print(n5,"nota(s) de R$ 5.00")
if n2:
    print(n2,"nota(s) de R$ 2.00")

if ms1:
    print(ms1,"moeda(s) de R$ 1.00")
if m50:
    print(m50,"moeda(s) de R$ 0.50")
if m25:
    print(m25,"moeda(s) de R$ 0.25")
if m10:
    print(m10,"moeda(s) de R$ 0.10")
if m5:
    print(m5,"moeda(s) de R$ 0.05")
if m01:
    print(m01,"moeda(s) de R$ 0.01")

