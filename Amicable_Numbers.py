a=int(input())
b=int(input())
sum=0
sum2=0
for i in range(1,a):
    if a%i==0:
        sum=sum+i
for j in range(1,b):
    if b%j==0:
        sum2=sum2+j
if a==sum2 and b==sum:
    print("Amicable")
else:
    print("Not Amicable")