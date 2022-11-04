n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
d=[]
for i in a:
    if i<b or i>c:
        d.append(i)
if len(d)>0:
    print(max(d))
else:
    print("-1")
