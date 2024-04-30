# https://leetcode.com/problems/plus-one/description/

def plusOne(digits):

    array = []
    for i in digits:
        array.append(str(i))
    
    combined = "".join(array)

    final_result = int(combined) + 1

    string_final_result = str(final_result)

    resulting_array = []

    for i in range(len(string_final_result)):
        resulting_array.append(int(string_final_result[i]))

    return resulting_array

print(plusOne([1,2,3]))