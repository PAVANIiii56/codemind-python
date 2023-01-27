n=int(input())
lst=list(map(int,input().split()))
d=[lst[i] for i in range(n) if i%2==0]
k=[str(lst[i]) for i in range(n) if i%2]
p=''
for i in range(len(d)):
    v=str(d[i]*k[i])
    p+=v
for i in p:
    print(i,end=" ")
