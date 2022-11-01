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
temp=n
for i in range(n-1,0,-1):
    if pal(i):
        d=i
        break
n=n+1
while n:
    if pal(n):
        e=n
        break
    n+=1
f=abs(temp-d)
g=abs(temp-e)
if f>g:
    print(e)
elif f<g:
    print(d)
else:
    print(d,e)