n=int(input())
rev=0
res=0
temp=n*n
while n:
    r=n%10
    rev=rev*10+r
    n=n//10
f=(rev*rev)
while f:
    g=f%10
    res=res*10+g
    f=f//10
if temp==res:
    print("True")
else:
    print("False")
 