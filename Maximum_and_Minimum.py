n=int(input())
arr=list(map(int,input().split()))
f=[]
flag=0
for i in arr:
    d=arr.count(i)
    if i==d:
        f.append(i)
        flag=1
if flag==1:
    print(min(f),max(f))
else:
    print("-1")