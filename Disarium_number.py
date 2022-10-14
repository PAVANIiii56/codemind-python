def dis(n):
    c=0
    while n:
        r=n%10
        c+=1
        n=n//10
    return c
def pal(n):
    d=0
    b=dis(n)
    while n:
        r=n%10
        d=d+r**b
        n=n//10
        b-=1
    return d
n=int(input())
if n==pal(n):
    print("True")
else:
    print("False")
