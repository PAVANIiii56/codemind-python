a,b=map(int,input().split())
arr=list(map(int,input().split()))
brr=list(map(int,input().split()))
c=[]
d=[]
for i in arr:
    for j in brr:
        if i==j:
            c.append(i)
for i in arr:
    for j in brr:
        if i not in c:
            if i not in d:
                d.append(i)
        if j not in c:
            if j not in d:
                d.append(j)
print(len(d))