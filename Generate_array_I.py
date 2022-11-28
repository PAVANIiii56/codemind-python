a=int(input())
arr=list(map(int,input().split()))
c=[]
d=[]
e=[]
f=[]
for i in range(1,len(arr),2):
    c.append(arr[i])
for j in range(0,len(arr),2):
    d.append(arr[j])
for i in d:
    i=str(i)
    e.append(i)
for i in range(len(e)):
    v=e[i]*c[i]
    f.append(v)
for i in f:
    for j in i:
        print(j,end=" ")