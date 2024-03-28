# https://www.codewars.com/kata/566fc12495810954b1000030/python

def nb_dig(n, d):
    squares = []
    numbers_with_target = []
    target_counter = 0

    for i in range(n + 1):
        squares.append(i * i)

    for numbers in squares:
        if str(d) in str(numbers):
            numbers_with_target.append(str(numbers))

    for nums in numbers_with_target:
        for i in range(len(nums)):
            if str(nums[i]) == str(d):
                target_counter += 1

    return target_counter

print(nb_dig(10, 1))

