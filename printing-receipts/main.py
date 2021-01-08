# Taking input of company details
companyname = input("Enter your company's name: ")
companyaddress = input("Enter your company's address: ")
# Taking input howmuch products are going to be in the receipt
n = int(input("Quantity of products: "))
# initialize arrays for prices and products
i=1
productlist = []
pricelist = []
# take inputs of price and all products and store them in  the array
while(i<=n): # used loop for taking input of many products and store them in a list
    product = input("Enter product name: ")
    price = int(input("Enter the price of the product: "))
    productlist.append(product) #product list
    pricelist.append(price)    # price list
    i = i+1

# message for printing at the footer of the receipt
msg = "Thanks for shopping with us today."

print("*"*50)
print(f"*\t\t\t{companyname}\t\t\t*")
print(f"*\t\t\t{companyaddress}\t\t\t*")
print(f"*{'='*48}*")
print('*\tProduct Name\tProduct Price\t\t *')
a = 0
total = 0
while(a<n):
    print(f"*\t{productlist[a]}\t\t{pricelist[a]}\t\t\t *")
    total = total+pricelist[a]
    a = a+1
print(f"*{'='*48}*")
print('*\t\t\tTotal\t\t\t *')
print(f"*\t\t\t{total}\t\t\t *")
print(f"*{'='*48}*")
print(f"*\t\t\t\t\t\t *\n*\t{msg}\t *\n*\t\t\t\t\t\t *")
print("*"*50)
    





