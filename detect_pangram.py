# https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python

# def is_pangram(s):
#     s = s.lower()
#     alphabet = 'abcdefghijklmnopqrstuvwxyz'
#     for char in alphabet:
#         if char not in s:
#             return False
#     return True
        

def is_pangram(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for letter in alphabet:
        if letter not in string:
            return False
    return True
print(is_pangram("abcdefghijklmnopqrstuvwxyz"))