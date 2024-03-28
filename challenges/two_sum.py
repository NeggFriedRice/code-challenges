def two_sum(numbers, target):
    sum = 0
    index1 = 0
    index2 = 1
    while sum != target:

        for i in range(index1 + 1, len(numbers)):
            sum = numbers[index1] + numbers[i]
            if sum == target:
                index2 = i
                break

        if sum != target:
            index1 += 1
            index2 = index1 + 1
            i = index1 + 1
            continue

        return (index1, index2)


print(two_sum([2, 2, 3], 4))