def word_converter(word_lower_case):
    # 97-122
    word_upper_case = ''
    for char in word_lower_case:
        value = ord(char)
        if 97 <= value <= 122:
            word_upper_case += chr(value-32)
        else:
            return '*'*len(word_lower_case)
    return word_upper_case


word = input('Enter a lower case word: ')
print(word, '->', word_converter(word))
