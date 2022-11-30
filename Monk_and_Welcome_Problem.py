n=int(input())
arr=list(map(int,input().split()))
brr=list(map(int,input().split()))
for i in range(len(arr)):
    c=arr[i]+brr[i]
    print(c,end=" ")