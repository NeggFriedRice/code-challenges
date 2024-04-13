def cc_check():
    cc = ""
    while True:
        cc = input("Please enter credit card number: ")

        if len(cc) == 16 or len(cc) == 15 or len(cc) == 13:
            break
    
    if cc[0] == '4':
        visa_check(cc)
    elif cc[0:2] == '34' or cc[0:2] == '37': 
        print('AMEX')
    elif cc[0:2] == '51' or cc[0:2] == '52' or cc[0:2] == '53' or cc[0:2] == '54' or cc[0:2] == '55':
        print('MASTER')

def visa_check(cc):
    second_nums_array = []
    
    reversed_cc = cc[::-1]

    for i in range(1, len(cc), 2):
        second_nums_array.append(str(int(reversed_cc[i]) * 2))

    # Find the product of the digits
    joined = "".join(second_nums_array)

    # Split array back out and find sum
    sum = 0
    for i in joined:
        sum += int(i)

    # Find nums that weren't multiplied by 2 in original string
    other_array = []
    for i in range(0, len(cc), 2):
        other_array.append(reversed_cc[i])

    final_sum = 0
    for i in other_array:
        final_sum += int(i)
    
    total_final_sum = final_sum + sum
    stringified = str(total_final_sum)

    if stringified[-1] == '0':
        print('VISA')
    else:
        print("Invalid")


cc_check()