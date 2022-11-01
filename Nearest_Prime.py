def prime(n):
    c=0
    if n==1:
        return False
    for i in range(2,(n//2)+1):
        if n%i==0:
            c+=1
    if c==0:
        return True
    else:
        return False
a=int(input())
for _ in range(a):
    n=int(input())
    temp=n
    for i in range(n-1,0,-1):
        if prime(i):
            b=i
            break
    for j in range(n,9999,1):
        if prime(j):
            c=j
            break
    if abs(n-b)>abs(n-c):
        print(c)
    elif abs(n-b)==abs(n-c):
        print(b)
    else:
        print(b)

        
        