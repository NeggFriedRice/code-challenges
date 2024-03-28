def solution(s):
    fixed_string = ""
    for letter in s:
        if letter.islower():
            fixed_string += letter
        else:
            fixed_string += " "
            fixed_string += letter
    return fixed_string


# Loop through string
# If encounters capital letter
# Insert space then capitalised letter
# Continue until end of string

print(solution("helloThere"))

