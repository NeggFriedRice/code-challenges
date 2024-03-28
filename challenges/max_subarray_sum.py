def max_sequence(arr):
    sum = 0
    sub_counter = 0
    starting_index = 0
    for i in range(len(arr)):
        sub_sum = sum + arr[i]

    if sub_sum > sum:
        sum = sub_sum
        sub_counter += 1

    else:
        starting_index = i

    
    print(sum)
    print(sub_counter)
    print(starting_index)


max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])

# Loop through starting at index 0,
# Keeping adding next element (add to counter with each add)
# If sum is greater than sum = 0, update sum, update index variable
# Once reaching end of array, reset counter to 0