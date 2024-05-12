# https://leetcode.com/problems/valid-palindrome/description/

def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    cleaned = "".join(char for char in s if char.isalnum())

    for i in range(len(cleaned) // 2):
        if cleaned[i].lower() != cleaned[-(i+1)].lower():
            return False
        
    return True
    
print(isPalindrome("A man, a plan, a canal: Panama"))