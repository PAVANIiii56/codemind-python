m,n=map(int,input().split())
mat=[[int(i) for i in input().split()] for j in range(m)]
d=[]
for i in mat:
    v=sum(i)
    d.append(v)
print(max(d))
    