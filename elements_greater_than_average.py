n=int(input())
a=list(map(int,input().split()))
c=0
d=sum(a)//n
for i in range(n):
    if d<=a[i]:
        c+=1
print(c)
