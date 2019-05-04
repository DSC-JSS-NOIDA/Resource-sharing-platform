import math
def gcd(e1,e2):
    if e2==0:
        return e1
    else:
        return gcd(e2, e1%e2)
tc = input()
for ii in range(tc):
    n,t,x,y,z = map(int,raw_input().split())
    a = (2*n)+1
    if t==1:
        if x==z:
            p = x
            q = a
        elif x<z:
            p = a-(y+1)
            q = a
        else:
            p = a-(y-1)
            q = a
    elif t==3:
        if x==z:
            p = x
            q = a
        elif x<z:
            p = a-(y-1)
            q = a
        else:
            p = a-(y+1)
            q = a
    else:
        p = a-(2*y)
        q = a
    f = gcd(p,q)
    p = p/f
    q = q/f
    print p,q
