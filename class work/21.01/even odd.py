even = [x for x in range(10) if  x%2==0 ]
odd = [x for x in range(10) if not (x%2==0) and (x%3==0)]
not_2_and_3 = [x for x in range(10) if not (x%2==0) and not (x%3==0)]
print(even,' - even nubers\n',odd,'- odd numbers, not %2==0 \n',not_2_and_3,' - not 2 and 3')
