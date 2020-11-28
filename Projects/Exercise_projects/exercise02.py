# Faulty Calculator
# Question:- Make a faulty calculator 45*3 = 555
# 56+9 = 77
# 56/6 = 4

a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
op = input("Enter the operator")
if a == 45 and b == 3 and op =="*":
    print(555)
elif a ==56 and b ==9 and op =="+":
    print(77)
elif a == 56 and b == 6 and op == "/":
    print(4)
elif op == "+":
    print(a+b)
elif op == "-":
    print(a-b)
elif op == "*":
    print(a*b)
elif op == "/":
    print(a/b)