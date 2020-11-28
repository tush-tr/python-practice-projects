import time
initial = time.time()
# print(initial)
for i in range(45):
    print("HEy")
# print("For loop time is: ",time.time()-initial,"seconds")
initial2 = time.time()
k = 0
while(k<45):
    print("Hey")
    time.sleep(2)
    k +=1
# print("While loop time is: ",time.time() - initial2,"seconds")
# localtime = time.asctime(time.localtime(time.time()))
# print(localtime)



