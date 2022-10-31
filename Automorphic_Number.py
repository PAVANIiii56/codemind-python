import math
n=int(input())
c=n*n
d=int(math.log10(n)+1)
e=c%math.pow(10,d)
if e==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")