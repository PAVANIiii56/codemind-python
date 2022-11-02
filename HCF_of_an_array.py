n=int(input())
a=list(map(int,input().split()))
d=min(a)
flag=0
for i in range(n):
    if a[i]%d!=0:
        flag=1
if flag==0:
    print(d)
else:
    print("1")
