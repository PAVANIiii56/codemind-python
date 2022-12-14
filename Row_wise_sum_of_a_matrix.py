a,b=map(int,input().split())
mat=[[int(i) for i in input().split()]for j in range(a)]
h=[]
for i in mat:
    f=sum(i)
    h.append(f)
print(*h)
 
