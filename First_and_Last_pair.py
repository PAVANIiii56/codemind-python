n=int(input())
arr=list(map(int,input().split()))
d=[]
f=[]
if n%2==0:
    for i in range((len(arr)//2)):
        d.append(arr[i])
        d.append(arr[len(arr)-i-1])
    print(*d)
elif n%2:
    for i in range((len(arr)//2)+1):
        f.append(arr[i])
        f.append(arr[len(arr)-i-1])
    f.remove(f[len(f)-1])
    f.append("0")
    print(*f)