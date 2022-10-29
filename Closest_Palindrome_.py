def pal(n):
    rev=0
    temp=n
    while n:
        r=n%10
        rev=rev*10+r
        n=n//10
    if rev==temp:
        return True
    else:
        return False
n=int(input())
tem=n
for i in range(n-1,0,-1):
    if pal(i)==True:
        a=i
        break
n=n+1
while n:
    if pal(n)==True:
        b=n
        break
    n+=1
d=abs(tem-a)
e=abs(tem-b)
if d==e:
    print(a,b)
elif d>e:
    print(b)
else:
    print(a)
    
