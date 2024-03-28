def order(sentence):
    sentence_split = sentence.split()
    
    num = 1
    ordered = []
    i = 0
    while i <= len(sentence_split):
        for index, words in enumerate(sentence_split):
            if str(num) in words:
                ordered.append(sentence_split[index])
                num += 1
        i += 1
    return " ".join(ordered)
print(order("is2 Thi1s T4est 3a"))