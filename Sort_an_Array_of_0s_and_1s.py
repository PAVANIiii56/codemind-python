n=int(input())
arr=list(map(int,input().split()))
c=0
for i in range(0,n):
    if arr[i]==0:
        c+=1
for i in range(0,c):
    arr[i]=0
for i in range(c,n):
    arr[i]=1
for i in range(0,n):
    print(arr[i],end=" ")