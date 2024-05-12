# https://leetcode.com/problems/single-number/description/

def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    number_check = []

    for num in nums:
        if num not in number_check:
            number_check.append(num)
        elif num in number_check:
            number_check.remove(num)

    return number_check[0]

print(singleNumber([1,0,1]))

    