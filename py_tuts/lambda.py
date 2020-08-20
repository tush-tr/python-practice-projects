# Lambda functions or anonymous functions
def add(a,b):
    return a+b
# it is just a method of creating functions
# minus = lambda x, y:x-y
# l = int(input("enter first number"))
# b = int(input("enter the second number:"))
# print(minus(l,b))
def a_first(a):
    return a[1]
a =[[1,14],[5,6],[8,24]]
a.sort(key=a_first)
# print(a)
# output- [[5, 6], [1, 14], [8, 24]]
# we can do this also with lambda
b = [[12,34],[12,4],[1,24]]
b.sort(key=lambda x:x[1])
print(b)


