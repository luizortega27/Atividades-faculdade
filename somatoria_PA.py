r = int(input())
n = int(input())
var = 1
calc = 1
soma = var + r
while soma <= n:
    var = var + r
    soma = var + r
    calc = calc + var
print("A somatoria da PA eh:",calc)   

