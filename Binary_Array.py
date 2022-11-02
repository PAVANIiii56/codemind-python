n=int(input())
a=list(map(int,input().split()))
flag=0
for p in range(n):
    if a[p]!=0 and a[p]!=1:
        flag=1
        break
if flag==0:
    print("True")
else:
    print("False")

