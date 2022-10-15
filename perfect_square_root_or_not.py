import math
n=int(input())
flag=0
for i in range(1,n,1):
    if n==i*i:
        flag=1
if flag==1:
    print("True")
else:
    print("False")