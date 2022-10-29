n=int(input())
temp=n
flag=0
for i in range(1,n+1):
    if n%i==0:
        b=n//i
        if b==i+1:
            flag=1
if flag==1:
    if temp==i*b:
        print("YES")
else:
    print("NO")
    