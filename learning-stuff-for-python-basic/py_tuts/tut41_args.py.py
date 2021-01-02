# def function_name_print(a,b,c,d):
#     print(a,b,c,d)
# function_name_print("Tushar", "Rahul","Sorabh","Ram")
l = ["Tushar","Rahul","Sorabh","Ram"]
n = " i am normal and students are as follows:"
# function using args
def my_function(*kids):
    print(type(kids))
    print("The youngest child is " + kids[0])
# function using args and using for loop for printing items in it
def fargs(*ar):
    for item in ar:
        print(item)
# calling function my_function()
print("Without loop using args")
# my_function("Emil", "Tobias", "Linus")
tp = ("Hello","vallo")
my_function(*tp)
# Calling function - fargs()
print("With loop using args")
fargs(*l)
# Function takes a normal argument and a arg argument
def funargs(normal,*args):
    print(normal)
    for i in args:
        print(i)
# using the funargs function
funargs(n,*l)
