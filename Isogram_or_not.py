n=input()
c=0
for i in n:
    if n.count(i)==1:
        c+=1
if len(n)==c:
    print(True)
else:
    print(False)