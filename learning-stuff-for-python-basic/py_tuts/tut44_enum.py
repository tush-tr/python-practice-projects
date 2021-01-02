l1 = ["Chowmeen","Pasta","Fried Rice","spoons"]
# i = 1
# for item in l1:
#     if i%2 is not 0:
#         print(f"Jarvish Please buy {item}")
#     i+=1

for index,item in enumerate(l1):
    if index%2 ==0:
        print(f"Jarvish Please buy {item}")


# The enumerate() function takes a collection (e.g. a tuple) and
# returns it as an enumerate object.

# The enumerate() function adds a counter as the key of the
# enumerate object.
# syntax --- enumerate(iterable, start)
x = ('apple', 'banana', 'cherry')
y = enumerate(x)
print(y)
for i in y:
    print(i)
