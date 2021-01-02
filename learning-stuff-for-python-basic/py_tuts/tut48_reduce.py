# ----------------------Reduce ---------------------
# The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list
# elements mentioned in the sequence passed along.This function is defined in “functools” module.

from functools import reduce
list1 = [1,2,3,4]
# Add all the elements in the list
# num = 0
# for i in list1:
#     num = num + i
# print(num)

num = reduce(lambda x,y:x*y,list1)
print(num)





