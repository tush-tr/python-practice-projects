# The map() function executes a specified function for each item in an iterable.
# The item is sent to the function as a parameter.




# n = ["34","45","23"]
# for items in range(len(n)):
#     n[items] = int(n[items])
# a = n[2]+2
# # print(a)
# n = list(map(int, n))
# # print(n)
# def sq(a):
#     return a*a
# num = [2,3,45,66,77,34,65,45]
# square = list(map(sq,num ))
# # print(square)
#
# newsquare = list(map(lambda x: x*x,num))
# print(newsquare)


def square(n):
    return n*n

def cube(n):
    return n*n*n

func = [square,cube]

num = [2,3,5,6,76,3,3,2]
for i in range(5):
    val = list(map(lambda x:x(i),func))
    print(val)

