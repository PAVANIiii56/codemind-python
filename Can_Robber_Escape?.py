n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(n):
    if a[i]>=n:
        c=1
        break
if c==1:
    print("NO")
else:
    print("YES")