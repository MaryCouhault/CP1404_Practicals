
word_to_num = {}
text = input("Text: ")

words = text.split()
for word in words:
    frequency = word_to_num.get(word, 0)
    word_to_num[word] = frequency + 1

words = list(word_to_num.keys())
words.sort()

max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, word_to_num[word]))