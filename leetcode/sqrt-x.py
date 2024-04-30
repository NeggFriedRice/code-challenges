# https://leetcode.com/problems/sqrtx/solutions/4083846/python-98-beats-6-lines-code-2nd-approach-simple-code/

def mySqrt(x):

    counter = 0
    result = 0

    while counter <= x:
        
        result = counter ** 2

        if result > x:
            return counter - 1
        elif result == x:
            return counter
        
        counter += 1
    
    return counter

print(mySqrt(2))