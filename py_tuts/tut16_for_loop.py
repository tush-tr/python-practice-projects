list1 = ["rahul",123, "sohil",12,2,3,4,5,6,1,0,23,]

# x = "Tushar"
# for point in x:
#     if point== "h":
#         break
for x in list1:
    if str(x).isnumeric() and x>6:
        print(x)
