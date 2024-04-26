def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """

    # Create map of letters to numbers
    m = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    # Initialise the final number
    result = 0

    # Loop through the roman numerals
    for i in range(len(s)):
        # Check condition, are we at the end of the string?
        # Check if the first character is bigger than the next, if yes, add it to the result

        if i < len(s) -1 and m[s[i]] > m[s[i+1]]:
            result += m[s[i]]
        else:
            result -= m[s[i]]

    return result

