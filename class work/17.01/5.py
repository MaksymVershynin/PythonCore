
list_numbers_fibo=[]
n=int(input('input amount of numbers\n'))
number_Fibbonachi=0
i=1
def fibo(n):
    for j in range(n):
        global number_Fibbonachi
        previous_number = number_Fibbonachi
        global i
        number_Fibbonachi+=i
        i=previous_number
        list_numbers_fibo.append(number_Fibbonachi)
    return list_numbers_fibo
print(fibo(n))
