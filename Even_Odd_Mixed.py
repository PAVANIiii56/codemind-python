n=int(input())
c=0
c1=0
c2=0
while n>0:
    r=n%10
    n=n//10
    c2+=1
    if r%2==0:
        c+=1
    elif r%2!=0:
       c1+=1
if c2==c:
    print("Even")
elif c2==c1:
    print("Odd")
else:
    print("Mixed")
