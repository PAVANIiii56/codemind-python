a=int(input())
b=int(input())
for i in range(a,b+1,1):
    n=i
    c=0
    d=0
    while(n>0):
        r=n%10
        n=n//10
        c+=1
        if(r==0):
            break
        if(i%r==0 and r!=0):
            d+=1
    if(c==d):
        print(i,end=' ')