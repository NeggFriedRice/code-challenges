# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    final_array = []

    for i in nums:
        if i not in final_array:
            final_array.append(i)

    return len(final_array)

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))