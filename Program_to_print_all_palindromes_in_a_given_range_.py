def pal(n):
    rev=0
    temp=n
    while n:
        r=n%10
        rev=rev*10+r
        n=n//10
    if temp==rev:
        return True
    else:
        return False
a=int(input())
b=int(input())
for i in range(a,b+1):
    if pal(i):
        print(i,end=" ")
    
    