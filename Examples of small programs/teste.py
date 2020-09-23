import wordcloud as wcl

def dict_of_frequencies (string):
    frequencies = {}
    bad_words = ['at', 'a', 'in', 'the', 'to', 'an', 'of', 'or', 'and', 'if']
    string = string.lower()
    string = string.split()
    for word in string:
        new_word = ""
        for character in word:
            if character.isalpha():
                new_word += character
        if new_word not in frequencies:
            frequencies[new_word] = 0
        frequencies[new_word] += 1

    for word in bad_words:
        if word in frequencies:
            del(frequencies[word])
    return frequencies


f = dict_of_frequencies("Before processing any text, you need to remove all the punctuation marks. To do this, you can go through each line of text, character-by-character, using the isalpha() method. This will check whether or not the character is a letter.")
cloud = wcl.WordCloud()
cloud.generate_from_frequencies(f)
cloud.to_file("img.jpg")