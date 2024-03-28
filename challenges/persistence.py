# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/python

def persistence(n):
    counter = 0
    sum_num = n
    while len(str(sum_num)) > 1:
        
        nums_list = []
        string_n = str(sum_num)
        for numbers in string_n:
            nums_list.append(numbers)
        
        result = 1
        for numbers in nums_list:
            result = result * int(numbers)

        sum_num = result
        counter += 1
    
    return counter


print(persistence(999))

# Convert initial number to string
# Split into new list
# Multiply numbers together
# Increase counter
# Loop from start