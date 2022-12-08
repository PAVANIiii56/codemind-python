n=int(input())
arr=list(map(int,input().split()))
f=[]
for i in arr:
    if i%2==0:
        break
    f.append(i)
print(sum(f))