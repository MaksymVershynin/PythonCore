last_number_of_list=int(input('input last number of list\n'))
number_Fibbonachi=0
i=1
while number_Fibbonachi<=last_number_of_list:
    print(number_Fibbonachi)
    previous_number = number_Fibbonachi
    number_Fibbonachi+=i
    i=previous_number  

# that was until last number of list

amount_of_numbers=int(input('input amount of numbers\n'))
number_Fibbonachi=0
i=1
for j in range(amount_of_numbers):
    print(number_Fibbonachi)
    previous_number = number_Fibbonachi
    number_Fibbonachi+=i
    i=previous_number 