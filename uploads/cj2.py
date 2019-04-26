tc = int(input())
for ii in range(tc):
    n = int(input())
    x = input()
    y = ''
    for i in range(2*n-2):
        if x[i]=='E':
            y+='S'
        else:
            y+='E'
    print("Case #"+str(ii+1)+":", y)
