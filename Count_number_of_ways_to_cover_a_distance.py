def fun(n) :
    if n<0:
       return 0
    if n==0:
       return 1
    return fun(n-3)+fun(n-2)+fun(n-1)
    
n=int(input())
print(fun(n))
 