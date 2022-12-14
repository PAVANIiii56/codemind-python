a,b=map(int,input().split())
mat=[[int(i) for i in input().split()]for j in range(a)]
v=list(zip(*mat))
h=[]
for i in v:
    f=sum(i)
    h.append(f)
print(max(h))
 
