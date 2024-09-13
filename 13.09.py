P=float(input())
a=1
aprim=P
przyblizenie=0.0000000000000000000001

while abs(a-aprim)>przyblizenie:
    a=(a+aprim)/2
    aprim=P/2
print(aprim)