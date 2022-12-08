for _ in range(int(input())):
    n=input()
    v=n[::-1]
    if n==v:
        if len(n)%2==0:
            print("YES EVEN")
        else:
            print("YES ODD")
    else:
        print("NO")