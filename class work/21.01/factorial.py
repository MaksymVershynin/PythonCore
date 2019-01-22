a=int(input("INPUT NUBER - "))
if (a==0 or a==1):
    print("Faktorial a! = 1")    #   because 0! = 1
else:
    b=1
    list=range(a+1)
    for i in list[1:(a+1)]:
        b=b*i
    print("Faktorial a! =", b)
