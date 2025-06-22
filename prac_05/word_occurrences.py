"""
word_to_count = {}
get words
repeat word in words
    if word in word_to_count
        value of word_to_count = value of word_to_count + 1
    else
        value of word_to_count = 1
max_width =-1
repeat word in keys of word_to_count
    width = length of word
    if width > max_width
        max_width = width
repeat word, word_count in items of word_to_count
    display word, value of word_count
"""
word_to_count = {}
words = input("Text: ")
for word in words.split():
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1
max_width =-1
for word in word_to_count.keys():
    width = len(word)
    if width > max_width:
        max_width = width
for word, word_count in word_to_count.items():
    print(f"{word:{max_width}} : {word_to_count[word]}")
