# def function1():
#     print("Do this work now")
# func2 = function1
# del function1
# func2()

# -------------Returning fucntions from a function---------
# def funcret(num):
#     if num ==0:
#         return print
#     if num==1:
#         return int
#     else:
#         return float
# a = funcret(0)
# print(a)
# def executor(func):
#     func("This")
#
# executor(print)


def dec1(func1):
    def nowexec():
        print("executing now")
        func1()
        print("Executed")
    return nowexec
@dec1
def who():
    print("I am Your friend")
# who = dec1(who)
who()








