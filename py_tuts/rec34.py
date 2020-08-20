# # Recursions
# def print2(str1):
#     print2(str1)
#     print( "this is "+ str1)
# print2("tushar")
#
# # if we are using the function print2(str1) inside this function then it'
# # s giving recursion error
#  Now we are making a new function called factorial
def factorial_iterative(r):
    '''

    :param r:Integer
    :return: n*n-1 * n-2 * n-3.........1
    '''
    fac =1
    for i in range(r):
        fac = fac *(i+1)
    return(fac)


# formula of factorial = 5*4*3*2*1
# n! = n*n-1*n-2*n-3.....1
# n! = n *(n-1)!
number = int(input("enter the number:"))
print("Factorial of the number using iterative method",factorial_iterative(number))
# Now we make the function using recursive method
def factorial_recursive(r):
    '''

    :param r:Integer
    :return: n*n-1 * n-2 * n-3.........1
    '''
    if r==1:
        return 1
    else:
        return r * factorial_recursive(r-1)
    # Logic of this function
# 5 * factorial_recursive(4)
# 5 * 4 * factorial_recursive(3)
# 5 * 4*3factorial_recursive(2)
# 5*4*3*2*factorial_recursive(1)
# 5*4*3*2*1 = 120
num = int(input("enter the number:"))
print("Factorial of the number using recursive method",factorial_recursive(num))
def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result
x = int(input("enter the number of your choice"))
print("\n\nRecursion Example Results")
print(tri_recursion(x))