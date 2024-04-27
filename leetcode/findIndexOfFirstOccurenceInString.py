# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """

    if needle not in haystack:
        return -1
    else:
        # Traverse the string with x number of 'shifts' where x is len(haystack) - len(needle); i.e. needle window can only shift 6 times before hitting the end of the string
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i