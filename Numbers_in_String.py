n=input()
k=[]
f=0
for i in n:
    if i.isdigit():
        k.append(i)
for i in k:
    v=int(i)
    f+=v
print(f)
    
       
        