# https://www.codewars.com/kata/5259b20d6021e9e14c0010d4/train/python

def reverse_words(text):
    words_array = text.split()
    print(words_array)

    result = ""
    for words in words_array:
        array = []
        for letter in words:
            array.insert(0, letter)

        reversed_word = "".join(array)
        print(reversed_word)
        result += reversed_word + " "
    return result[0:-1]

    
reverse_words("hello there")
    
    