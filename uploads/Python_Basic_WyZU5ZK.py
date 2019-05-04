tc = int(input())
for ii in range(tc):
    n = int(input())
    c,o,d,e,h,f=0,0,0,0,0,0
    for i in range(n):
        x = input()
        for ff in x:
            if ff=='c':
                c+=1
            if ff=='o':
                o+=1
            if ff=='d':
                d+=1
            if ff=='e':
                e+=1
            if ff=='h':
                h+=1
            if ff=='f':
                f+=1
    c,e = c/2,e/2
    a = min(c,o,d,e,h,f)
    print(int(a))
        
