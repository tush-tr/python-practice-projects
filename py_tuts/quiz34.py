# fibonic sequence
# 0 1 1 2 3 5 8 13
# every numbers comes from the sum of previuous two numbers
# write a function of nth fabonic sequence
def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+ fibonacci(n-2)
num = int(input("enter the number"))
print(fibonacci(num))
