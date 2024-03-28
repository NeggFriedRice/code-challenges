def stray(arr):
    for number in arr:
        if arr.count(number) == 1:
            return number

print(stray([3, 2, 2, 2, 2]))
# Iterate over array
# Take first number, assign to variable
# Check if next number is the same, if not, assign number