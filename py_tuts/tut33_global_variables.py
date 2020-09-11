# l = 10 #global variable
# def function1(n):
#     global l
#     l = l+2
#     m = 24 #local variable
#     print(l,m)
#     print(n,"I have printed")
# function1("This is me")
# # print(l)
# # first focus on local variable then global

def clu():
    x = 23
    def rah():
        global x
        x = 88
    print("before calling rah()",x)
    rah()
    print("after calling rah()",x)

clu()
print(x)