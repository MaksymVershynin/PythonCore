number=int(input('input number: '))
i=0
while number>=1:
    i+=number%10
    number//=10
print(i)