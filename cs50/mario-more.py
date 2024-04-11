# Create a pyramid given an integer

# ...#
# ..##
# .###
# ####

def create_pyramid():

    while True:
        num = int(input("Enter a number between 1 and 8! \n"))

        if num >= 1 and num <= 8:
            # Execute print
            for i in range(num):
                string = ""
                string += (num - (i + 1)) * " "
                string += (i + 1) * "#"
                print(string + " " + string[::-1])
            break
        else:
            continue

create_pyramid()