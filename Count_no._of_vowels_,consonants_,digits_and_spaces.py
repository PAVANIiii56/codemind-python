n=input()
h=n.split(" ")
l=['a','e','i','o','u']
c,c1,c2=0,0,0
for i in n:
    if i.isdigit():
        c+=1
for i in n:
    if i not in l:
        c2+=1
for i in n:
    if i in l:
        c1+=1
g=len(h)-1
print("Vowels:",c1)
print("Consonants:",len(n)-c1-c-g)
print("Digits:",c)
print("White spaces:",len(h)-1)
    
        