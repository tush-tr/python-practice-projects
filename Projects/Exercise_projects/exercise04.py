#print a star pattern
print("Pattern printing")
rows = int(input("Enter the number of rows you want:"))
print("Enter 1 or 0")
boolv = input("1 for True and 0 for false")
if boolv=="1":
    for i in range(0,rows+1):
        print("*"*int(i))
else:
    for i in range(rows,0,-1):
        print("*"*int(i))
