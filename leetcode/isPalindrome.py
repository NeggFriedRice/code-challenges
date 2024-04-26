def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    arr = []
    stringified = str(x)
    for i in range(len(stringified)):
        arr.append(stringified[i])

    for i in range(len(arr)):
        if arr[i] != arr[len(arr) - 1 - i]:
            return False
    
    return True


print(isPalindrome(1000001))