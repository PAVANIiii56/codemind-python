a,b=map(int,input().split())
arr=list(map(int,input().split()))
brr=list(map(int,input().split()))
c=[]
d=[]
for i in arr:
    for j in brr:
        if i==j:
            c.append(j)
for i in arr:
    if i not in c:
        if i not in d:
            d.append(i)
for j in brr:
    if j not in c:
        if j not in d:
            d.append(j)
print(*d)