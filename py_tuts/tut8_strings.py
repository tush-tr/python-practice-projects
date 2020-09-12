# printing a string 10 times
st = 10 * "Hello "
print("10 times after string --",st)
sumofstring = "u"+"t"
print(sumofstring)
# using r
print("Hey \nano")
print(r"Hey \nano") #notice the r
# Creating a new string
any = "he is done"
# Length of the string
length = len(any)
print("Length of the string any is",length)
# string slicing
a = any[-5:-2:]
b = any[5:8]
if(a==b):
    print("a and b are equal")
    print("Value is-- ",a)
print("true if all characters are alphanumerical")
print("isalnum() function-- ",any.isalnum())
print("check string is in alphabet")
print(any.isalpha())
print("string end with specified value")
print(any.endswith("done")) # True
print("No. of times a specified value occures in string")
print(any.count("e"))
print("Converts first character to upper case")
print(any.capitalize())
print("Search the string")
print(any.find("is"))
print("Convert string in lower case")
print(any.lower())
print("Upper case")
print(any.upper())
print("replace")
print(any.replace("is","are"))
ra = "HeLLo aLL"
print(ra.swapcase())






