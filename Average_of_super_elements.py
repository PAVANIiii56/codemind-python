n=int(input())
arr=list(map(int,input().split()))
f=[]
flag=0
for i in arr:
    d=arr.count(i)
    if i==d:
        if i not in f:
            f.append(i)
            flag=1
if flag==1:
    print("{:.2f}".format(sum(f)/len(f)))
else:
    print("-1")