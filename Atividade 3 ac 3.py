n=int(input())
a=1
var=0
while a<=n:
    var=var+(1/a**2)
    a +=1
print("{:.6f}".format(var))