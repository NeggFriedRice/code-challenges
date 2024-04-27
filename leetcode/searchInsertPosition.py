# https://leetcode.com/problems/search-insert-position/description/

def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

    ## (My) Brute force implementation
    # for i in range(len(nums)):
    #     if target == nums[i]:
    #         return i
        
    # for j in range(len(nums)):
    #     if target < nums[j]:
    #         return j
    #     else:
    #         continue
    
    # return len(nums)

    ## (Solutions) Alternate (and more efficient solution) - binary search

    # Specify left and right start search
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return left
                



print(searchInsert([1,3,5,6], 5))

    