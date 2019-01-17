list=input("Please, input your list")
for i in list:
    a=0
    if (int(i)%2==1):
        print("in list we have neparni")
        break
    a=1
if (a==1):
    print("in list we DONT have neparni")
