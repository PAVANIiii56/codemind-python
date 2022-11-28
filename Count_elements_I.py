a,b=map(int,input().split())
arr=list(map(int,input().split()))
brr=list(map(int,input().split()))
c=[]
d=[]
for i in arr:
    for j in brr:
        if i==j:
            if i not in c:
                c.append(i)
print(len(c))