a=int(input())
while a>9:
    res=0
    while a:
         r=a%10
         res=res+r*r
         a=a//10
    a=res
if res==1:
    print("True")
else:
    print("False")