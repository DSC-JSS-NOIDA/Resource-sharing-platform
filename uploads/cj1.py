tc = int(input())
for ii in range(tc):
    n = input()
    a = ''
    for i in range(len(n)):
        if n[i]=='4':
            a = a + '1'
            n = n[:i]+'3'+n[i+1:]
        else:
            a = a + '0'
    print("Case #"+str(ii+1)+":", int(n), int(a))
