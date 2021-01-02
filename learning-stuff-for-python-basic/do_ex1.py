# print a star pattern using recursion

def star(n):
    if n==0:
        return ""
    else:
        print(" * "*n)
        star(n-1)


star(10)