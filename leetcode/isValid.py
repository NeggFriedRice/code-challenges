# https://leetcode.com/problems/valid-parentheses/


## First attempt before neetcode
# def isValid(s):
#     """
#     :type s: str
#     :rtype: bool
#     """

#     m = {
#         "(": ")",
#         "[": "]",
#         "{": "}"
#     }

#     # Loop over the string
#     for i in range(0, len(s) - 1, 2):
#         # If open bracket is not equal to the close bracket in the next slot, return False
#         if s[i] == "(" and s[i + 1] == ")":
#             return True
#         elif s[i] == "[" and s[i + 1] == "]":
#             return True
#         elif s[i] == "{" and s[i + 1] == "}":
#             return True
#         else:
#             return False
        
# print(isValid("()"))

def isValid(s):
    stack = []

    if len(s) <= 1:
        return False
    elif len(s) == 2 and s[0] in "([{" and s[1] in "([{":
        return False
    else:
        for bracket in s:
            if bracket in "([{":
                stack.append(bracket)
            elif bracket == ")":
                if len(stack) > 0 and stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif bracket == "]":
                if len(stack) > 0 and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            elif bracket == "}":
                if len(stack) > 0 and stack[-1] == "{":
                    stack.pop()
                else:
                    return False
        
        if len(stack) > 0:
            return False
        else:
            return True
            

print(isValid("[[["))