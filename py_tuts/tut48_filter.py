#-----------------------------Filter---------------------------------------
# The filter() function returns an iterator were the items are filtered through a
# function to test if the item is accepted or not.



ist1 = [1,2,3,455,56,643,45523,3,4]
def isgreater(n):
    return n>5
g_5 = list(filter(isgreater,list1))
print(g_5)


