# https://leetcode.com/problems/length-of-last-word/description/

def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    arr = s.split()

    return len(arr[-1])

print(lengthOfLastWord("hello world"))
