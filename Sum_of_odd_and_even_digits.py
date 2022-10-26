n=int(input())
a=list(map(int,input().split()))
sum=0
sum1=0
diff=0
for i in range(n):
    if i%2==0:
        sum=sum+a[i]
    elif i%2:
        sum1=sum1+a[i]
diff=abs(sum-sum1)
if diff==0:
    print("YES")
else:
    print("NO")