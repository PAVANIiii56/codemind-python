a,b=map(int,input().split())
for i in range(1,b+1):
    if a>0 and b>0:
        if i%2:
            print(a,'x',i,'=',a*i)
        