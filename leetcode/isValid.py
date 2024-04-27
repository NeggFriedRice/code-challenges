# https://leetcode.com/problems/valid-parentheses/

def isValid(s):
    """
    :type s: str
    :rtype: bool
    """

    m = {
        "(": ")",
        "[": "]",
        "{": "}"
    }

    # Loop over the string
    for i in range(0, len(s) - 1, 2):
        # If open bracket is not equal to the close bracket in the next slot, return False
        if s[i] == "(" and s[i + 1] == ")":
            return True
        elif s[i] == "[" and s[i + 1] == "]":
            return True
        elif s[i] == "{" and s[i + 1] == "}":
            return True
        else:
            return False
        
print(isValid("()"))