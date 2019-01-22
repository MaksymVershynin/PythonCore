amount_of_numbers=int(input('Input amount of numbers\n'))
list_of_numbers=[int(input('input number\n')) for i in range(amount_of_numbers)]
print('max number in input list is {}\nmin number in input list is {}'. format(max(list_of_numbers),min(list_of_numbers)))