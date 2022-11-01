def prime(n):
    c=0
    for i in range(2,(n//2)+1):
        if n%i==0:
            c+=1
    if c==0:
        return True
    else:
        return False
def pal(n):
    temp=n
    rev=0
    while n:
        r=n%10
        rev=rev*10+r
        n=n//10
    if temp==rev:
        return True
    else:
        return False
n=int(input())
n=n+1
while True:
    if prime(n) and pal(n):
        print(n)
        break
    n+=1
    
    