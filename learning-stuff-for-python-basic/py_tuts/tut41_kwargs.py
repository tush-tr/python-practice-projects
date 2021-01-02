d1 = {"Rohan":"Html specialist","Ram":"C programmer","Rahul":"database guy"}
li = ["Rahul","Sohan","mohan","Lallan"]
normal = "I am normal argument and dict is:-"
def fun(normal, *args, **kwargs):
    print(normal)
    for item in args:
        print(item)
    for key, value in kwargs.items():
        print(f"{key} --- {value}")

# calling function?
fun(normal,*li,**d1)
 # Another example
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")