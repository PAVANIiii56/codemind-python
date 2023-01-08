d=[]
for i in range(int(input())):
    str=input()
    d.append(str)
v=d.count('X++')
l=d.count('++X')
s=d.count('X--')
j=d.count('--X')
print(v+l-(s+j))
