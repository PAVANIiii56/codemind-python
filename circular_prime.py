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
def pal(n):
    rev=0
    temp=n
    while n:
        r=n%10
        rev=rev*10+r
        n=n//10
    return rev
n=int(input())
if prime(n) and prime(pal(n)) :
    print("circular prime")
elif prime(n):
    if prime(pal(n))==False:
        print("prime but not a circular prime")
else:
    print("not prime")
    